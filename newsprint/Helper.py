class Helpers():
    def compare_dates_iso(self, date1, date2):
        date1 = parser.parse(date1)
        date2 = parser.parse(date2)
        return date1 > date2

    def merge_two_dicts(self, x, y):
        """Given two dictionaries, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z
