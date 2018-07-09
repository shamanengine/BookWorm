class Badge:
    """Representation of a badge with title, prompt, index and description"""

    index_high: float
    index_low: float

    def __init__(self, title, prompt, index_low, index_high, description):
        self.title = title
        self.prompt = prompt
        self.index_low = float(index_low)
        self.index_high = float(index_high)
        self.description = description

    def __repr__(self):
        return (
            "Title: \t\t\t{title}"
            "\nPrompt: \t\t{prompt}"
            "\nIndex: \t\t\t[{index_low}; {index_high})"
            "\nDescription: \t{description}"
        ).format(title=self.title, prompt=self.prompt, index_low=self.index_low, index_high=self.index_high,
                 description=self.description)


if __name__ == '__main__':
    badge = Badge("A", "AA", 0.25, 0.5, "descr")
    print(badge)
