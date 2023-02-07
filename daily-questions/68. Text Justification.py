class Solution:
    def formatWords(self, curr_space, curr_line, lines, maxWidth):
        temp = []
        extra_space = maxWidth - curr_space
        spots = max(1, len(lines[curr_line]) - 1)
        gap = extra_space // spots
        length = len(lines[curr_line])
        modulo = extra_space % spots
        
        for i in range(length):
            temp.append(lines[curr_line][i])
            if i != length - 1:
                space = gap + 1 if modulo > 0 else gap
                dec = 1 if modulo > 0 else 0
                temp.append(" " * space)
                modulo -= dec
        if length == 1:
            temp.append(" " * gap)
           
        return "".join(temp)
        
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = defaultdict(list)
        line, space = 0, 0
        for word in words:
            if line not in lines:
                lines[line].append(word)
                space += len(word)
            else:
                if space + len(word) + 1 <= maxWidth:
                    lines[line].append(" " + word)
                    space +=  (len(word) + 1)
                else:
                    lines[line].append(space)
                    line += 1
                    space = len(word)
                    lines[line].append(word)         
        
        
        last_line = max(lines.keys())
        answer = []
        for i in range(last_line):
            curr_space = lines[i].pop()
            line = self.formatWords(curr_space, i, lines, maxWidth)
            answer.append(line)
        temp = []
        line = lines[last_line]
        length = len(line)
        space = 0

        # processing the last line
        for i in range(length):
            if i != length - 1:
                temp.append(line[i] )
                space += (len(line[i]))
            else:
                
                extra = maxWidth - space - len(line[i])
                temp.append(line[i])
                temp.append(" " * extra)
        answer.append(''.join(temp))      
                
        return answer
            
