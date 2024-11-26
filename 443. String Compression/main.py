class Solution:
    def compress(self, chars: List[str]) -> int:
        read,write,length=0,0,len(chars)
        while read<length:
            read_next=read+1
            while read_next<length and chars[read_next]==chars[read]:
                read_next+=1
            chars[write]=chars[read]
            write+=1
            if(read_next-read>1):
                char=str(read_next - read)
                print(char)
                for c in char:
                    print(c)
                    chars[write]=c
                    write+=1
            read=read_next
        return write
            

        