def main():

    X=int(input())

    if X==1 or X==2 or X==3:

        print(1)

    else:

        li=[]

        for p in range(2,10):

            for n in range(2,100):

                if n**p<=X:

                    li.append(n**p)

                else:

                    break

        li.sort(reverse=True)

        print(li[0])

if __name__=="__main__":

    main()