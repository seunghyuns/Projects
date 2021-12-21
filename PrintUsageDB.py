
import pymssql
conn = pymssql.connect(server="10.10.4.37:14233",user='genuine',password='ASD!!axzC$',database='EMSF', as_dict=False)
cursor = conn.cursor()


def FindQuery(Arguments):
    Query = """select B.DeptName, A.EmpName from _TDAEmp AS A             
                  LEFT OUTER join _tcaUser AS C WITH(NOLOCK)  ON A.EmpSeq = C.EmpSeq
                  LEFT OUTER join _tdadept AS B WITH(NOLOCK)  ON C.DeptSeq = B.DeptSeq
                  where A.empid = '{}'""".format(Arguments)
                  
    Query2 = """SELECT	B.DeptName, A.EmpName FROM	_TDAEmp AS A 
		        JOIN _tcaUser AS C WITH(NOLOCK) ON A.EmpSeq = C.EmpSeq
		        JOIN _tdadept AS B WITH(NOLOCK) ON C.DeptSeq = B.DeptSeq
                WHERE	A.empid = '{}'
                UNION ALL
                SELECT	 T1.ValueText	AS DeptName
		                ,T0.Remark		AS EmpName
                FROM		_TDAUMinor	AS	T0	WITH (NOLOCK)
		        LEFT OUTER JOIN	_TDAUMinorValue	AS	T1	WITH (NOLOCK)	ON	T0.MajorSeq = T1.MajorSeq	AND	T0.MinorSeq	=	T1.MinorSeq		AND	T1.Serl	=	1000001
                WHERE	T0.CompanySeq = '1'		
                AND		T0.MajorSeq	=	1026002
                AND		T0.IsUse = '1'
                AND		T0.MinorName = '{}'""".format(Arguments,Arguments)
    return Query2

def dbConnect():
    conn = pymssql.connect(server="10.10.4.37:14233",user='genuine',password='ASD!!axzC$',database='EMSF', as_dict=False)
    cursor = conn.cursor()



def dbExcute(excuteName):
    result = cursor.execute(excuteName)
    return result 
    
    
def dbFetchOne():
    result = cursor.fetchone()
    return result
    
    
def dbClose():
    conn.close()