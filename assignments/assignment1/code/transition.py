class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """Adds the arc (b, relation, s) to A, and pops Sigma. That is, draw an arc between the next node on the buffer and the next node on the stack, with the label relation"""
        if not conf.buffer or not conf.stack:
            return -1
        else:
            b = conf.buffer[0]
            s = conf.stack[-1]
            # preconditions:
            # s is not the artificial root node 0
            if s == 0:
                return -1
            # and does not already have a head
            for item in conf.arcs:
                if item[2] == s:
                    return -1

            conf.buffer.pop(0)
            conf.stack.pop()
            conf.arcs.append((b, relation, s))


    @staticmethod
    def right_arc(conf, relation):
        """Adds the arc (s, relation, b) to A, and pushes b onto Sigma"""
        if not conf.buffer or not conf.stack:
            return -1
        else:
            s = conf.stack[-1]
            b = conf.buffer.pop(0)
            conf.stack.append(b)
            conf.arcs.append((s, relation, b))


    @staticmethod
    def reduce(conf):
        """Pops Sigma"""
        if not conf.buffer:
            return -1
        else:
            s = conf.stack[-1]
            # precondition: s has a head
            hasHead = False
            for item in conf.arcs:
                if item[2] == s:
                    hasHead = True

            if hasHead:
                conf.stack.pop()
            else:
                return -1


    @staticmethod
    def shift(conf):
        """Removes b from B and adds it to Sigma"""
        if not conf.buffer:
            return -1
        else:
            conf.stack.append(conf.buffer.pop(0))
