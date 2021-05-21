import datetime


class DateHelpers:
    @staticmethod
    def convert_from_ms(timestamp_ms):
        float_ts = float(timestamp_ms)
        if float_ts/1000000000000 > 1:
            float_ts = float_ts/1000
            return datetime.datetime.fromtimestamp(float_ts)
        return datetime.datetime.fromtimestamp(float_ts)

