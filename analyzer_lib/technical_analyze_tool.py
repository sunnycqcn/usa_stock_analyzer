def calc_sma(df, days):
    return df.rolling(window=days).mean()


def calc_macd(df):
    ema12 = calc_ema(df, 12)
    ema26 = calc_ema(df, 26)
    return ema12 - ema26


def calc_macd2(df):
    macd = calc_macd(df)
    macd_sig = calc_sma(macd, 9)
    return macd - macd_sig
def mavol(df):
    VOL1 = calc_vol(df, 1)
    MAVOL1 = calc_vol(df, 3)
    MAVOL1 = calc_vol(df, 7)
    MAVOL1 = calc_vol(df, 13)

def calc_ema(df, span):
    return df.ewm(span=span, adjust=False).mean()
def calc_vol(df, span):
    return df.ewm(span=span, adjust=False).mean()

def calc_regression_line_slope(data):
    """
    Calculate slope(a) of regression line calculated by given data.
    """
    if None in data:
        return None

    x_list = list(range(len(data)))
    y_list = data

    n = len(x_list)
    x_ave = sum(x_list) / n
    y_ave = sum(y_list) / n

    x_dispersion = sum([(xi - x_ave) ** 2 for xi in x_list]) / n
    covariance = sum([(xi - x_ave) * (yi - y_ave) for xi, yi in zip(x_list, y_list)]) / n

    return covariance / x_dispersion


def is_all_prices_are_higher_than_trend(prices, trend):
    """
    Return true if all price is over the trend line.
    """
    if None in prices or None in trend:
        return False

    diff = [prices[i] - trend[i] for i in range(len(prices))]

    for d in diff:
        if d < 0:
            return False
    return True


def is_golden_cross(v1, v2):
    if None in [v1, v2]:
        return False
    return v1<0 and v2>0


def is_dead_cross(v1, v2):
    if None in [v1, v2]:
        return False
    return v1>0 and v2<0


def has_single_cross(data):
    count = 0
    for i in range(1, len(data)):
        if is_golden_cross(data[i-1], data[i]) or is_dead_cross(data[i-1], data[i]):
            count = 1
    if count == 1:
        return True
    else:
        return False
