from textwrap import wrap
from pickle import load,dump
from os import makedirs,system
from time import localtime
from datetime import datetime
from msvcrt import getch,putch
from sys import argv
class Book:
    def __init__(self,AN,Ti,Au,Pb,Pr,Ed,Pg,DP):
        self.AccNo=AN
        self.Title=Ti
        self.Author=Au
        self.Publisher=Pb
        self.Price=Pr
        self.Edition=Ed
        self.Pages=Pg
        self.DOP=DP
        self.Issued=False
        self.Active=True
    def modify(self,Ti,Au,Pb,Pr,Ed,Pg):
        self.Title=Ti if Ti else self.Title
        self.Author=Au if Au else self.Author
        self.Publisher=Pb if Pb else self.Publisher
        self.Price=Pr if Pr else self.Price
        self.Edition=Ed if Ed else self.Edition
        self.Pages=Pg if Pg else self.Pages
class Member:
    def __init__(self,MN,Nm,Ad,DB,Mob,DJ):
        self.MNo=MN
        self.MName=Nm
        self.MAddress=Ad
        self.MDOB=DB
        self.MMobNo=Mob
        self.MDOJ=DJ
        self.MBIssued=False
        self.MActive=True
    def modify(self,Nm,Ad,DB,Mob):
        self.MName=Nm if Nm else self.MName
        self.MAddress=Ad if Ad else self.MAddress
        self.MDOB=DB if DB else self.MDOB
        self.MMobNo=Mob if Mob else self.MMobNo
class Issue:
    def __init__(self,IN,Acc,MN,DI):
        self.IssNo=IN
        self.BAccNo=Acc
        self.MNo=MN
        self.DOI=DI
        self.DOR=""
        self.Fine=0
    def Return(self,DR):
        self.DOR=DR
        self.Calc_Fine()
    def Calc_Fine(self):
        d1=datetime(*(map(int,self.DOI.split('/'))[::-1]))
        d2=datetime(*(map(int,self.DOR.split('/'))[::-1]))
        dif=str(d2-d1)
        day=0
        try:
            day=int(dif[:dif.find(' ')])
        except:
            day=0
        self.Fine=(day-14)*2 if day>14 else 0
class Library:
    pth=""
    def __init__(self,pt="D:\\"):
        self.pth=pt+'Library Data\\'
        for x in ('Books\\','Members\\','Issues\\'):
            try:
                makedirs(self.pth+x)
            except:
                pass
    def AH(self,No,Md='rb'):
    	ext=No[0]
       	if ext not in "BMI" or ext=='':
            return None
    	de=dict(zip(('B','M','I'),('Books\\','Members\\','Issues\\')))
    	tf=None
    	try:
    	   tf=open(self.pth+de[ext]+"%s.dat"%No,Md)
    	except:
    	   pass
    	return tf
    def NNo(self,ext='',minn=1):
        nno=minn
        while True:
            tf=self.AH(ext+str(nno))
            if not tf:
            	yield ext+str(nno)
            else:
            	nno+=1
            	tf.close()
    def Get_Date(self):
        return "{2:0>2}/{1:0>2}/{0:0>2}".format(*localtime())
    def Book_Add(self):
        try:
            NAcc=self.NNo('B')
            Acc=next(NAcc)
            print "Enter Accession No: %s"%Acc
            Ti=raw_input("Enter Title: ")
            Au=raw_input("Enter Author: ")
            Pb=raw_input("Enter Publisher: ")
            Pr=input("Enter Price: Rs ")
            Ed=input("Enter Edition: ")
            Pg=input("Enter No of Pages: ")
            DP=self.Get_Date()
            if Ti and Au and Pb and Pr and Ed and Pg and DP:
                bk=Book(Acc,Ti,Au,Pb,Pr,Ed,Pg,DP)
                tf=self.AH(Acc,'wb+')
                dump(bk,tf)
                tf.close()
                print "Book has been Added..."
            else:
                print "Sorry! Not Enough Details to Add Book!"
                print "Please Try Again..."
        except:
            print "Sorry! Book Could not be Added!"
            print "Please Try Again..."
    def Book_Remove(self):
    	try:
    		Acc='B'+raw_input("Enter Accession No: B")
    		tf=self.AH(Acc)
    		if not tf:
    			print "Book doesn't Exists..."
    			return
    		bk=load(tf)
    		tf.close()
    		if not bk.Active:
    			print "Book has been Already Removed..."
    			return
    		elif bk.Issued:
    			print "Book is Issued to Some Member..."
    			return
    		bk.Active=False
    		tf=self.AH(Acc,'wb+')
    		dump(bk,tf)
    		tf.close()
    		print "Book has been Removed..."
    	except:
    		print "Sorry! Book Could not be Removed!"
    		print "Please Try Again..."
    def Book_Modify(self):
        try:
            Acc='B'+raw_input("Enter Accession No: B")
            tf=self.AH(Acc)
            if not tf:
                print "Book doesn't Exists..."
                return
            bk=load(tf)
            tf.close()
            if not bk.Active:
                print "Book has been Removed..."
                return
            elif bk.Issued:
                print "Book is Issued to Some Member..."
                return
            Ti=raw_input("Enter Title: ")
            Au=raw_input("Enter Author: ")
            Pb=raw_input("Enter Publisher: ")
            Pr=raw_input("Enter Price: Rs ")
            Pr=0 if not Pr else int(Pr)
            Ed=raw_input("Enter Edition: ")
            Ed=0 if not Ed else int(Ed)
            Pg=raw_input("Enter No of Pages: ")
            Pg=0 if not Pg else int(Pg)
            bk.modify(Ti,Au,Pb,Pr,Ed,Pg)
            tf=self.AH(Acc,'wb+')
            dump(bk,tf)
            tf.close()
            print "Book has been Modified..."
        except:
            print "Sorry! Book Could not be Modified!"
            print "Please Try Again..."
    def Mem_Add(self):
        try:
            NMN=self.NNo('M')
            MNo=next(NMN)
            print "Enter Member No: %s"%MNo
            Nm=raw_input("Enter Name: ")
            Ad=raw_input("Enter Address: ")
            DB=raw_input("Enter Date of Birth: ")
            Mob=raw_input("Enter Mobile No: ")
            DJ=self.Get_Date()
            if Nm and Ad and DB and Mob and DJ:
                mem=Member(MNo,Nm,Ad,DB,Mob,DJ)
                tf=self.AH(MNo,'wb+')
                dump(mem,tf)
                tf.close()
                print "Member has been Added..."
            else:
                print "Sorry! Not Enough Details to Add Member!"
                print "Please Try Again..."
        except:
            print "Sorry! Member Could not be Added!"
            print "Please Try Again..."
    def Mem_Remove(self):
        try:
            MNo='M'+raw_input("Enter Member No: M")
            tf=self.AH(MNo)
            if not tf:
                print "Member doesn't Exists..."
                return
            mem=load(tf)
            tf.close()
            if not mem.MActive:
                print "Member has been Already Removed..."
                return
            elif mem.MBIssued:
                print "Member is Issued Some Book..."
                return
            mem.MActive=False
            tf=self.AH(MNo,'wb+')
            dump(mem,tf)
            tf.close()
            print "Member has been Removed"
        except:
            print "Sorry! Member Could not be Removed!"
            print "Please Try Again..."
    def Mem_Modify(self):
        try:
            MNo='M'+raw_input("Enter Member No: M")
            tf=self.AH(MNo)
            if not tf:
                print "Member doesn't Exists..."
                return
            mem=load(tf)
            tf.close()
            if not mem.MActive:
                print "Member has been Removed..."
                return
            elif mem.MBIssued:
                print "Member is Issued Some Book..."
                return
            Nm=raw_input("Enter Name: ")
            Ad=raw_input("Enter Address: ")
            DB=raw_input("Enter Date of Birth: ")
            Mob=raw_input("Enter Mobile No: ")
            mem.modify(Nm,Ad,DB,Mob)
            tf=self.AH(MNo,'wb+')
            dump(mem,tf)
            tf.close()
            print "Member has been Modified..."
        except:
            print "Sorry! Member Could not be Modified!"
            print "Please Try Again..."
    def Book_Issue(self):
        try:
            NIN=self.NNo('I')
            IN=next(NIN)
            print "Enter Issue No: %s"%IN
            Acc='B'+raw_input("Enter Accession No: B")
            tf=self.AH(Acc)
            if not tf:
                print "Book doesn't Exists..."
                return
            bk=load(tf)
            tf.close()
            if not bk.Active:
                print "Book has been Already Removed..."
                return
            elif bk.Issued:
                print "Book is Issued to Some Member..."
                return
            MNo='M'+raw_input("Enter Member No: M")
            tf=self.AH(MNo)
            if not tf:
                print "Member doesn't Exists..."
                return
            mem=load(tf)
            tf.close()
            if not mem.MActive:
                print "Member has been Removed..."
                return
            elif mem.MBIssued:
                print "Member is Issued Some Book..."
                return
            DI=self.Get_Date()
            isu=Issue(IN,bk.AccNo,mem.MNo,DI)
            bk.Issued=True
            mem.MBIssued=True
            tf=self.AH(IN,'wb+')
            dump(isu,tf)
            tf.close()
            tf=self.AH(bk.AccNo,'wb+')
            dump(bk,tf)
            tf.close()
            tf=self.AH(mem.MNo,'wb+')
            dump(mem,tf)
            tf.close()
            print "Book has been Issued..."
        except:
            print "Sorry! Book Could not be Issued!"
            print "Please Try Again..."
    def Book_Return(self):
        try:
            IN='I'+raw_input("Enter Issue No: I")
            tf=self.AH(IN)
            if not tf:
                print "Issue doesn't Exits..."
                return
            isu=load(tf)
            tf.close()
            DR=self.Get_Date()
            isu.Return(DR)
            if isu.Fine>0:
                print "Fine: Rs %s"%isu.Fine
            tf=self.AH(IN,'wb+')
            dump(isu,tf)
            tf.close()
            tf=self.AH(isu.BAccNo)
            bk=load(tf)
            tf.close()
            bk.Issued=False
            tf=self.AH(isu.BAccNo,'wb+')
            dump(bk,tf)
            tf.close()
            tf=self.AH(isu.MNo)
            mem=load(tf)
            tf.close()
            mem.MBIssued=False
            tf=self.AH(isu.MNo,'wb+')
            dump(mem,tf)
            tf.close()
            print "Book has been Returned..."
        except:
            print "Sorry! Book Could not be Returned!"
            print "Please Try Again..."
    def Get_Books(self):
        bkl=list()
        Acc=1
        while True:
            tf=self.AH('B'+str(Acc))
            if not tf:
                break
            bk=load(tf)
            bkl.append(bk)
            tf.close()
            Acc+=1
        return bkl
    def Get_Members(self):
        meml=list()
        MNo=1
        while True:
            tf=self.AH('M'+str(MNo))
            if not tf:
                break
            mem=load(tf)
            meml.append(mem)
            tf.close()
            MNo+=1
        return meml
    def Get_Issues(self):
        isul=list()
        IN=1
        while True:
            tf=self.AH('I'+str(IN))
            if not tf:
                break
            isu=load(tf)
            isul.append(isu)
            tf.close()
            IN+=1
        return isul
lib=None
wdt=110
mwdt=30
def Print_Head():
    system("cls")
    print '*'*wdt
    print ('*'*5+" SHERLOCK'S LIBRARY "+'*'*5).center(wdt)
    print '-'*wdt
def Print_Menu(head,lst):
    lst=lst+("Exit",)
    print
    print ' '*6+'-'*mwdt
    print ' '*6+'|{0:_^{lnt}}|'.format('::'+head+'::',lnt=mwdt-2)
    print ' '*6+'|{0: ^{lnt}}|'.format('',lnt=mwdt-2)
    for no in range(len(lst)):
        print ' '*6+'| {0: <{lnt}}|'.format('Enter %d.'%(no+1)+lst[no],lnt=mwdt-3)
    print ' '*6+'-'*mwdt
def Get_Input(rnge,prompt="Enter Choice: "):
    for c in prompt:
        putch(c)
    srnge=map(str,rnge)
    st=''
    while True:
        ch=getch()
        if ch=='\r':
            if len(st)!=0:
                break
        elif ch=='\b':
            if len(st)!=0:
                putch('\b')
                putch(' ')
                putch('\b')
                st=st[:-1]
        elif st+ch in srnge:
            st+=ch
            putch(ch)
    print
    return st
def Wait():
    print
    for c in 'Press Any Key to Close....': putch(c)
    getch()
def LibMang():
    head="MAIN MENU"
    menu=("Book Maintenance","Member Maintenance","Book Issue/Return","Report Portal","Search Portal")
    df={1:Book_Maint,2:Mem_Maint,3:Book_IR,4:Report_Port,5:Search_Port}
    ch='1'
    while ch in "12345":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,7))
        print
        if ch!='6':
            ch=df[int(ch)]()
    print '-'*wdt
    print ('*'*5+" THANK YOU "+'*'*5).center(wdt)
    print '*'*wdt
    getch()
def Book_Maint():
    head="BOOK MAINTENANCE"
    menu=("Add Book","Remove Book","Modify Book","Go Back")
    df={1:lib.Book_Add,2:lib.Book_Remove,3:lib.Book_Modify}
    ch='1'
    while ch in "123":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,6))
        print
        if ch in "123":
            df[int(ch)]()
            Wait()
    return '6' if ch=='5' else '1'
def Mem_Maint():
    head="MEMBER MAINTENANCE"
    menu=("Add Member","Remove Member","Modify Member","Go Back")
    df={1:lib.Mem_Add,2:lib.Mem_Remove,3:lib.Mem_Modify}
    ch='1'
    while ch in "123":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,6))
        print
        if ch in "123":
            df[int(ch)]()
            Wait()
    return '6' if ch=='5' else '1'
def Book_IR():
    head="BOOK ISSUE/RETURN"
    menu=("Issue Book","Return Book","Search Portal","Go Back")
    df={1:lib.Book_Issue,2:lib.Book_Return,3:Search_Port}
    ch='1'
    while ch in "123":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,6))
        print
        if ch in "12":
            df[int(ch)]()
            Wait()
        elif ch=='3':
            ch=df[int(ch)]()
            ch='5' if ch=='6' else ch
    return '6' if ch=='5' else '1'
def Report_Port():
    head="REPORT PORTAL"
    menu=("Books Report","Members Report","Issues Report","Go Back")
    df={1:Books_Report,2:Members_Report,3:Issues_Report}
    ch='1'
    while ch in "123":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,6))
        print
        if ch in "123":
            df[int(ch)]()
            Wait()
    return '6' if ch=='5' else '1'
def Scale(l,x):
    if x>=len(l):
        return ''
    return l[x]
def Display(sz,hd,lt,la=[]):
    st=""
    for x in range(len(sz)):
        st+="{%d:^%s}|"%(x,sz[x])
    st=st[:-1]
    print 
    print '='*wdt
    l=[]
    for x in range(len(hd)):
        l.append(wrap(hd[x],width=sz[x]))
    mxl=max(map(len,l))
    for x in range(mxl):
        pt=tuple(map(Scale,l,[x]*len(sz)))
        print st.format(*pt)
    print '='*wdt
    pos=0;n=1
    while n<st.count('^'):
        pos=st.index('^',pos+1)
        if n in la:
            st=st[:pos]+'<'+st[pos+1:]
        n+=1
    for pl in lt:
        l=[]
        for x in range(len(pl)):
            l.append(wrap(pl[x],width=sz[x]))
        mxl=max(map(len,l))
        for x in range(mxl):
            pt=tuple(map(Scale,l,[x]*len(sz)))
            print st.format(*pt)
        print '.'*wdt
    print '='*wdt
def Books_Display(bkl):
    sz=(6,20,15,10,9,7,5,16,6,6)
    hd=("Acc No","Title","Author","Publisher","Price(Rs)","Edition","Pages","Date of Purchase","Issued","Active")    
    YN={True:"Yes",False:"No"}
    lt=[]
    for bk in bkl:
        bl=[]
        bl.append(bk.AccNo)
        bl.append(bk.Title)
        bl.append(bk.Author)
        bl.append(bk.Publisher)
        bl.append(str(bk.Price))
        bl.append(str(bk.Edition))
        bl.append(str(bk.Pages))
        bl.append(bk.DOP)
        bl.append(YN[bk.Issued])
        bl.append(YN[bk.Active])
        lt.append(tuple(bl))
    Display(sz,hd,lt,[2,3,4])
def Books_Report(): Books_Display(lib.Get_Books())
def Members_Display(meml):
    sz=(6,22,24,13,10,15,6,6)
    hd=("Mem No","Name","Address","Date of Birth","Mobile No","Date of Joining","Issued","Active")
    YN={True:"Yes",False:"No"}
    lt=[]
    for mem in meml:
        ml=[]
        ml.append(mem.MNo)
        ml.append(mem.MName)
        ml.append(mem.MAddress)
        ml.append(mem.MDOB)
        ml.append(mem.MMobNo)
        ml.append(mem.MDOJ)
        ml.append(YN[mem.MBIssued])
        ml.append(YN[mem.MActive])
        lt.append(tuple(ml))
    Display(sz,hd,lt,[2,3])
def Members_Report(): Members_Display(lib.Get_Members())
def Issues_Display(isul):
    sz=(12,14,12,25,25,16)
    hd=("Iss No","BAcc No","Mem No","Date of Issue","Date of Return","Fine(Rs)")
    YN={True:"Yes",False:"No"}
    lt=[]
    for isu in isul:
        il=[]
        il.append(isu.IssNo)
        il.append(isu.BAccNo)
        il.append(isu.MNo)
        il.append(isu.DOI)
        il.append(isu.DOR)
        il.append(str(isu.Fine))
        if il[-2]=='': il[-2]='-'
        if il[-1]=='0': il[-1]='-'
        lt.append(tuple(il))
    Display(sz,hd,lt)
def Issues_Report(): Issues_Display(lib.Get_Issues())
def Search_Port():
    head="SEARCH PORTAL"
    menu=("Search Book","Search Member","Search Issue","Go Back")
    df={1:Search_Book,2:Search_Member,3:Search_Issue}
    ch='1'
    while ch in "123":
        Print_Head()
        Print_Menu(head,menu)
        ch=Get_Input(range(1,6))
        print
        if ch in "123":
            df[int(ch)]()
            Wait()
    return '6' if ch=='5' else '1'
def Search_Book():
    bkl=lib.Get_Books()
    print "Enter Details to Filter:"
    Acc='B'+raw_input("Enter Accession No: B")
    Ti=raw_input("Enter Title: ")
    Au=raw_input("Enter Author: ")
    Pb=raw_input("Enter Publisher: ")
    Pr=raw_input("Enter Price: Rs ")
    Pr=0 if not Pr else int(Pr)
    Ed=raw_input("Enter Edition: ")
    Ed=0 if not Ed else int(Ed)
    Pg=raw_input("Enter No of Pages: ")
    Pg=0 if not Pg else int(Pg)
    fl=[]
    for bk in bkl:
        match=1
        match*=int(not Acc or Acc in bk.AccNo)
        match*=int(not Ti or Ti in bk.Title)
        match*=int(not Au or Au in bk.Author)
        match*=int(not Pb or Pb in bk.Publisher)
        match*=int(not Pr or Pr==bk.Price)
        match*=int(not Ed or Ed==bk.Edition)
        match*=int(not Pg or Pg==bk.Pages)
        if match:
            fl.append(bk)
    Books_Display(fl)
def Search_Member():
    meml=lib.Get_Members()
    print "Enter Details to Filter:"
    MNo='M'+raw_input("Enter Member No: M")
    Nm=raw_input("Enter Name: ")
    Ad=raw_input("Enter Address: ")
    DB=raw_input("Enter Date of Birth: ")
    Mob=raw_input("Enter Mobile No: ")
    fl=[]
    for mem in meml:
        match=1
        match*=int(not MNo or MNo in mem.MNo)
        match*=int(not Nm or Nm in mem.MName)
        match*=int(not Ad or Ad in mem.MAddress)
        match*=int(not DB or DB in mem.MDOB)
        match*=int(not Mob or Mob in mem.MMobNo)
        if match:
            fl.append(mem)
    Members_Display(fl)
def Search_Issue():
    isul=lib.Get_Issues()
    print "Enter Details to Filter:"
    IN='I'+raw_input("Enter Issue No: I")
    Acc='B'+raw_input("Enter Accession No: B")
    MNo='M'+raw_input("Enter Member No: M")
    DI=raw_input("Enter Date of Issue: ")
    DR=raw_input("Enter Date of Return: ")
    Fn=raw_input("Enter Minimum Fine Amount: Rs ")
    Fn=0 if not Fn else int(Fn)
    fl=[]
    for isu in isul:
        match=1
        match*=int(not IN or IN in isu.IssNo)
        match*=int(not Acc or Acc in isu.BAccNo)
        match*=int(not MNo or MNo in isu.MNo)
        match*=int(not DI or DI==isu.DOI)
        match*=int(not DR or DR==isu.DOR)
        match*=int(Fn<=isu.Fine)
        if match:
            fl.append(isu)
    Issues_Display(fl)
#Main
if __name__=='__main__':
    plc=argv[0]
    lib=Library(plc[:plc.rfind('\\')+1])
    LibMang()