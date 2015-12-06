class AB(object):
    def __init__(self):
        object.__init__(self)

    def createString(self, N, K):
        queue = [[K,]]
        while queue:
            head = queue[0]
            cnt =  head[0] + len(head)
            print 'debug[8]', queue, head, cnt
            raw_input()
            if cnt <= N:
                break
            else:
                del queue[0]
                expand = (head[-1] + 1) / 2 
                for i in range(head[-1]-1, expand-1, -1):
                    queue.append(head[:-1]+[i, head[-1]-i])

        result = ''
        if queue:
            lst = [True] +  [False] * (cnt - 1)
            for i in head[1:]:
                lst[cnt-i-1] = True
            for i in range(cnt):
                result = result + ('A' if lst[i] else 'B')
            result = result + 'A' * (N - cnt)
        return result

def main():
    obj = AB()
    print obj.createString(13, 29)

if __name__ == '__main__':
    main()
