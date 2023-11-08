

class CompositeCursor:

    @classmethod
    def build(cls, cursor, cursorType, orderedTypes):
        if not cursor and cursorType == orderedTypes[-1]:
            return None

        index = orderedTypes.index(cursorType)
        nextType = cursorType if cursor else orderedTypes[index + 1]

        return "{entityType}/{cursor}".format(
            entityType=nextType,
            cursor=cursor or "",
        )

    @classmethod
    def parse(cls, compositeCursor, orderedTypes):
        if not compositeCursor:
            return orderedTypes[0], None

        entityType, cursor = compositeCursor.split("/")
        return entityType, cursor or None
