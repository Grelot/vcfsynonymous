class CdsSeq:
    def __init__(self, seqid, start, end, sequence):
        self.seqid = seqid
        self.start = start
        self.end = end
        self.sequence = sequence
        self.codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]