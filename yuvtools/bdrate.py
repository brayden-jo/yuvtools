import numpy as np
import math
import scipy.interpolate


def bdrate2(metric_set1, metric_set2):
  """
  BJONTEGAARD    Bjontegaard metric calculation adapted
  Bjontegaard's metric allows to compute the average % saving in bitrate
  between two rate-distortion curves [1].  This is an adaptation of that
  method that fixes inconsistencies when the curve fit operation goes awry
  by replacing the curve fit function with a Piecewise Cubic Hermite
  Interpolating Polynomial and then integrating that by evaluating that
  function at small intervals using the trapezoid method to calculate
  the integral.

  metric_set1 - list of tuples ( bitrate,  metric ) for first graph
  metric_set2 - list of tuples ( bitrate,  metric ) for second graph
  """

  if not metric_set1 or not metric_set2:
    return 0.0

  try:

    # pchip_interlopate requires keys sorted by x axis. x-axis will
    # be our metric not the bitrate so sort by metric.
    metric_set1.sort(key=lambda tup: tup[1])
    metric_set2.sort(key=lambda tup: tup[1])

    # Pull the log of the rate and clamped psnr from metric_sets.
    log_rate1 = [math.log(x[0]) for x in metric_set1]
    metric1 = [100.0 if x[1] == float('inf') else x[1] for x in metric_set1]
    log_rate2 = [math.log(x[0]) for x in metric_set2]
    metric2 = [100.0 if x[1] == float('inf') else x[1] for x in metric_set2]

    # Integration interval.  This metric only works on the area that's
    # overlapping.   Extrapolation of these things is sketchy so we avoid.
    min_int = max([min(metric1), min(metric2)])
    max_int = min([max(metric1), max(metric2)])

    # No overlap means no sensible metric possible.
    if max_int <= min_int:
      return 0.0

    # Use Piecewise Cubic Hermite Interpolating Polynomial interpolation to
    # create 100 new samples points separated by interval.
    lin = np.linspace(min_int, max_int, num=100, retstep=True)
    interval = lin[1]
    samples = lin[0]
    v1 = scipy.interpolate.pchip_interpolate(metric1, log_rate1, samples)
    v2 = scipy.interpolate.pchip_interpolate(metric2, log_rate2, samples)

    # Calculate the integral using the trapezoid method on the samples.
    int_v1 = np.trapz(v1, dx=interval)
    int_v2 = np.trapz(v2, dx=interval)

    # Calculate the average improvement.
    avg_exp_diff = (int_v2 - int_v1) / (max_int - min_int)

  except (TypeError, ZeroDivisionError, ValueError, np.RankWarning) as e:
    return 0

  # Convert to a percentage.
  avg_diff = (math.exp(avg_exp_diff) - 1) * 100

  return avg_diff