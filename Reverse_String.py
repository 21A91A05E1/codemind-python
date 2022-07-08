class reverse():
    def rev_sent(self,sentence):
        words=sentence.split()
        reverse_sentence=" ".join(reversed(words))
        print(reverse_sentence)
c=reverse()
c.rev_sent(input())