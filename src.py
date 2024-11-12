def makePatient(age, sex, trestbps, chol, fbs, thalach, oldpeak):
    """Creates a Patient ADT."""
    return ("HDPT", {
        'age': age,
        'sex': sex,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'thalach': thalach,
        'oldpeak': oldpeak
    })


def patientInfo(p):
    """Returns detailed patient information if the input is a valid Patient ADT."""
    if not isPatient(p):
        return {"error": "Invalid Patient ADT"}
    return {
        "Age": getPatientAge(p),
        "Gender": getPatientSex(p),
        "Resting Blood Pressure (systolic)": getPatientTres(p),
        "Cholesterol Level": getPatientChol(p),
        "Fasting Blood Sugar (1 if >120 mg/dL)": getPatientFbs(p),
        "Maximum Heart Rate Achieved": getPatientTlach(p),
        "ST Depression (exercise vs rest)": getPatientST(p)
    }


def getPatientAge(pt):
    """Retrieves patient's age."""
    return pt[1]['age']


def getPatientSex(pt):
    """Retrieves patient's sex."""
    return pt[1]['sex']


def getPatientTres(pt):
    """Retrieves patient's resting systolic blood pressure."""
    return pt[1]['trestbps']


def getPatientChol(pt):
    """Retrieves patient's cholesterol level."""
    return pt[1]['chol']


def getPatientFbs(pt):
    """Retrieves patient's fasting blood sugar."""
    return pt[1]['fbs']


def getPatientTlach(pt):
    """Retrieves patient's maximum heart rate achieved."""
    return pt[1]['thalach']


def getPatientST(pt):
    """Retrieves patient's ST depression level."""
    return pt[1]['oldpeak']


def isPatient(pt):
    """Checks if the input is a valid Patient ADT."""
    if type(pt) == tuple and len(pt) == 2 and pt[0] == "HDPT":
        if 'age' in pt[1] and 'sex' in pt[1] and 'trestbps' in pt[1]:
            return True
    return False


def isEmptyPt(pt):
    """Checks if the Patient ADT is empty."""
    if not isPatient(pt):
        return True
    return False

# Part 2: Health Conditions
def isHypertensive(age, sex, trestbps):
    """Determines if a patient is hypertensive based on age, sex, and blood pressure."""
    if 1 <= age <= 3 and trestbps >= 98:
        return True
    if age >= 4:
        if (sex == 'male' or sex == 'M') and trestbps >= 140:
            return True
        if (sex == 'female' or sex == 'F') and trestbps >= 140:
            return True
    return False


def hasHighCholesterol(chol):
    """Checks if the patient's cholesterol level is high."""
    return chol >= 220


def isPhysicallyInactive(thalach, sex, age):
    """Determines if a patient is physically inactive based on heart rate, sex, and age."""
    if sex == 'male' or sex == 'M':
        if age > 35 and thalach >= 220:
            return True
        elif age <= 35 and thalach >= 230:
            return True
    elif sex == 'female' or sex == 'F':
        if age > 35 and thalach >= 226:
            return True
        elif age <= 35 and thalach >= 236:
            return True
    return False


def ptScores(PSLst):
    """Returns the list of patient-score tuples from the score list."""
    return PSLst[1]


def makePscore(ptLst):
    """Creates a score list."""
    return ['PS', []]


def calPScore(pt):
    """Calculates the overall risk score for a patient."""
    score = 0.0
    sex = getPatientSex(pt)
    age = getPatientAge(pt)
    trestbps = getPatientTres(pt)
    chol = getPatientChol(pt)
    thalach = getPatientTlach(pt)

    if isHypertensive(age, sex, trestbps):
        score += 4
    if hasHighCholesterol(chol):
        score += 3
    if isPhysicallyInactive(thalach, sex, age):
        score += 2
    if sex == 'male' or sex == 'M':
        score += 1.5
    elif sex == 'female' or sex == 'F':
        score += 1

    return score


def addPatient(PSLst, pt):
    """Adds a patient and their score to the score list."""
    ptScores(PSLst).append((pt, calPScore(pt)))


def getCritical(PSLst):
    """Retrieves patients with scores above 7.0."""
    critical = []
    for i in ptScores(PSLst):
        pt_info = i[0]
        score = i[-1]
        if score > 7.0:
            critical.append(pt_info)
    return critical


def getNonCrit(PSLst):
    """Retrieves patients with scores below 5.0."""
    non_critical = []
    for i in ptScores(PSLst):
        pt_info = i[0]
        score = i[-1]
        if score < 5.0:
            non_critical.append(pt_info)
    return non_critical


def isScore(Score):
    """Checks if the score is valid."""
    if Score >= 12:
        return False
    return True


def isEmptyScore(Score):
    """Checks if the score list is empty."""
    return len(ptScores(PSLst)) == 0


def makePtQueue(Qtype):
    """Creates a patient queue based on type (1: Critical, 2: Non-Critical, 3: Waiting)."""
    tag = {1: "C-Q", 2: "N-Q", 3: "W-Q"}.get(Qtype, "Unknown-Q")
    return (tag, [])


def contentsQ(q):
    """Returns the contents of a queue."""
    return q[1]


def frontPtQ(q):
    """Returns the first patient in the queue."""
    return q[1][0] if not isEmptPtQ(q) else None


def addToPtQ(pt, q):
    """Adds a patient to the queue."""
    q[1].append(pt)


def removeFromPtQ(q):
    """Removes the first patient from the queue."""
    if not isEmptPtQ(q):
        q[1].pop(0)


def isPatientQ(q):
    """Checks if the input is a valid patient queue."""
    return type(q) == tuple and q[0] in ["C-Q", "N-Q", "W-Q"] and isinstance(contentsQ(q), list)


def isEmptPtQ(q):
    """Checks if the queue is empty."""
    return len(contentsQ(q)) == 0


def makePatientStack():
"""Returns an empty Patient Stack as a tuple, where the first part
of the tuple is a tag ‘HDS’ and the second part of the tuple is
an empty list."""
    return ("HDS", [])


def contentsStack(stk):
"""Takes a Patient Stack as input and returns the list of patient
records in the Stack."""
    return stk[1]


def topPtStack(stk):
"""Takes a Patient Stack as an input and returns the element on
the top of the stack."""
    if isEmptyPtStack(stk):
        return None
    return stk[1][0]


def pushPtStack(pkt, stk):
"""Removes the first patient from the stack."""
    stk[1].insert(0, pkt)


def popPtStack(stk):
"""Removes the first patient from the stack."""
    if not isEmptyPtStack(stk):
        stk[1].pop(0)



def isPtStack(stk):
"""Checks if the input is a valid patient stack."""
    return isinstance(stk, tuple) and len(stk) == 2 and stk[0] == "HDS" and isinstance(stk[1], list)


def isEmptyPtStack(stk):
"""Checks to see if a given Patient Stack is empty."""
    return len(stk[1]) == 0



def sortPatients(patientList,patientStack,patientQueue):
  """
    Sorts patients in the score list based on risk score.
    High scores (Critical patients) come first.
    """
    contentsStack(patientStack).sort(key=lambda pt: calPScore(pt), reverse=True)
    contentsQ(patientQueue).sort(key=lambda pt: calPScore(pt), reverse=True)



def analyzePatients(patient_lst):
 """
    Allocates patients to appropriate queues based on their risk score:
    - Score > 7: Critical Queue.
    - 5 <= Score <= 7: Waiting Queue.
    - Score < 5: Non-Critical Queue.
    """
    pqueue = makePtQueue(1) + makePtQueue(2) + makePtQueue(3)
    pstack = makePatientStack()

    for patient_record in patient_lst:
        patient = makePatient(*patient_record)
        score = calPScore(patient)

        if patient in getCritical(score):
            addToPtQ(patient, pqueue)
            pushPtStack(patient, pstack)
        elif patient in getNonCrit(score):
            addToPtQ(patient, pqueue)
        else:
            addToPtQ(patient, pqueue)

    sortPatients(patient_lst, pstack, pqueue)
    return contentsQ(pqueue)



if __name__ == "__main__":

    number_of_patients = int(input())

    
    # Get Each Patient Information From Input As A String, and Create a List of Patient Tuples as
    # ('age', 'sex', 'trestbps', 'chol', 'fbs', 'thalach', 'oldpeak')
    # Store list of tuples as *ip_lst*
    ip_lst = []
    for i in range(number_of_patients):
        patient_info = input().strip().split()
        age = int(patient_info[0])
        sex = patient_info[1]  # No conversion needed
        trestbps = int(patient_info[2])
        chol = int(patient_info[3])
        fbs = int(patient_info[4])
        thalach = int(patient_info[5])
        oldpeak = float(patient_info[6])
        ip_lst.append((age, sex, trestbps, chol, fbs, thalach, oldpeak))

       print(ip_lst)

    # Store list of Patient Score Tuples as *PSLst*
    p_lst = []
    for ip_info in ip_lst:
        p_lst += [makePatient(int(ip_info[0]), ip_info[1], int(ip_info[2]), \
                              int(ip_info[3]), int(ip_info[4]), int(ip_info[5]), float(ip_info[6]))]
    PSLst = makePscore(p_lst)
    for p in p_lst:
        addPatient(PSLst, p)

    
    # returns a queue of all patients in order of highest to lowest overall risk score.
    fQueue = analyzePatients(ip_lst)

   
    # Print the queue

    print(fQueue)

    
    # Print the risk score of the patient at the BACK of the queue with the LOWEST OVERALL RISK SCORE
    print(calPScore(fQueue[-1]))

    
    # Print the risk score of the patient at the front of the queue with the HIGHEST OVERALL RISK SCORE
    print(calPScore(fQueue[0]))
