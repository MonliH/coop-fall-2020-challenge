class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = [0]
        self.history_position = 0

    def _insert_history(self, change: int):
        """Replace a value in the history if it exists, otherwise append"""
        if len(self.history) > self.history_position:
            self.history[self.history_position] = change
        else:
            self.history.append(change)

        # Increment history position (we inserted an element)
        self.history_position += 1

    def _update_value(self, amount: int):
        """Update value based on history position

        Positional Arguments:
        amount -- how far back into the history to travel.

        Notes:
        * `amount` should be negative to travel backwards, positive to travel forwards
        """


        adjusted_idx = (self.history_position+amount, self.history_position)

        # Sum all of the actions done between the range we want to undo/redo
        undone_actions = sum(self.history[min(adjusted_idx):max(adjusted_idx)])

        # Check if undoing or redoing, and update the value accordingly
        self.value -= undone_actions if amount < 0 else -undone_actions
        self.history_position += amount

    def add(self, num: int):
        """Add to value

        Positional Arguments:
        num -- value to add
        """
        self.value += num
        self._insert_history(+num)

    def subtract(self, num: int):
        """Subtract from value

        Positional Arguments:
        num -- value to subtract
        """
        self.value -= num
        self._insert_history(-num)

    def undo(self):
        """Undo one change to value"""
        self._update_value(-1)

    def redo(self):
        """Redo one change to value"""
        self._update_value(+1)

    def bulk_undo(self, steps: int):
        """Undo multiple changes to value

        Positional Arguments:
        steps -- amount of actions to undo
        """
        self._update_value(-steps)

    def bulk_redo(self, steps: int):
        """Redo multiple changes to value

        Positional Arguments:
        steps -- amount of actions to redo
        """

        self._update_value(+steps)
