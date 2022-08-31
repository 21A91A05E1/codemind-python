class reverse():
    def rev_sent(self,sentence):
        words="".join(reversed(sentence))
        reverse_sentence="".join(words)
        print(reverse_sentence)
c=reverse()
c.rev_sent(input())