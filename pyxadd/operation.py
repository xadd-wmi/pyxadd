class Operation:
    @classmethod
    def compute_terminal(cls, pool, node1, node2):
        # deal with NaN?
        # special cases
        # two terminals
        raise NotImplementedError()


class Multiplication(Operation):
    @classmethod
    def compute_terminal(cls, pool, node1, node2):
        # TODO deal with NaN?
        from pyxadd.diagram import TerminalNode
        if node1.node_id == pool.zero_id or node2.node_id == pool.zero_id:
            return pool.zero_id
        elif node1.node_id == pool.one_id:
            return node2.node_id
        elif node2.node_id == pool.one_id:
            return node1.node_id
        elif isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode):
            return pool.terminal(node1.expression * node2.expression)
        return None


class Summation(Operation):
    @classmethod
    def compute_terminal(cls, pool, node1, node2):
        # TODO deal with NaN?
        from pyxadd.diagram import TerminalNode
        if node1.node_id == pool.zero_id:
            return node2.node_id
        elif node2.node_id == pool.zero_id:
            return node1.node_id
        elif node1.node_id == pool.pos_inf_id or node1.node_id == pool.neg_inf_id:
            return node1.node_id
        elif node2.node_id == pool.pos_inf_id or node2.node_id == pool.neg_inf_id:
            return node2.node_id
        elif isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode):
            return pool.terminal(node1.expression + node2.expression)
        return None


class LogicalOr(Operation):
    @classmethod
    def compute_terminal(cls, pool, node1, node2):
        # TODO deal with NaN?
        from pyxadd.diagram import TerminalNode
        if isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode) \
                and ((node1.node_id != pool.zero_id and node1.node_id != pool.one_id)
                     or (node2.node_id != pool.zero_id and node2.node_id != pool.one_id)):
            raise RuntimeError("Nodes must be one or zero")

        if node1.node_id == pool.zero_id:
            return node2.node_id
        elif node1.node_id == pool.one_id:
            return pool.one_id
        elif node2.node_id == pool.zero_id:
            return node1.node_id
        elif node2.node_id == pool.one_id:
            return pool.one_id
        elif isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode):
            raise RuntimeError("Cases should be covered")
        return None


class LogicalAnd(Operation):
    @classmethod
    def compute_terminal(cls, pool, node1, node2):
        # TODO deal with NaN?
        from pyxadd.diagram import TerminalNode
        if isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode) \
                and ((node1.node_id != pool.zero_id and node1.node_id != pool.one_id)
                     or (node2.node_id != pool.zero_id and node2.node_id != pool.one_id)):
            raise RuntimeError("Nodes must be one or zero")

        if node1.node_id == pool.one_id:
            return node2.node_id
        elif node1.node_id == pool.zero_id:
            return pool.zero_id
        elif node2.node_id == pool.one_id:
            return node1.node_id
        elif node2.node_id == pool.zero_id:
            return pool.zero_id
        elif isinstance(node1, TerminalNode) and isinstance(node2, TerminalNode):
            raise RuntimeError("Cases should be covered")
        return None