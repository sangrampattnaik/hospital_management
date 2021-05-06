def calculate_unique_patient(Model):
    result = []
    unique_patient_month_wise = {}
    for o in range(1,13):
        remove_duplicate_patient = {}
        p = Model.objects.filter(date__month=o).values('account_id','date','patient_id').distinct()
        for patient in p:
            account_id = patient['account_id']
            patient_id = patient['patient_id']
            if account_id in remove_duplicate_patient:
                if patient_id not in remove_duplicate_patient[account_id]:
                    remove_duplicate_patient[account_id].append(patient_id)
            else:
                remove_duplicate_patient[account_id] = [patient_id]
        if remove_duplicate_patient:
            unique_patient_month_wise[o] = remove_duplicate_patient
            result.append(unique_patient_month_wise)
    return result[0]



def count_unique_physician(Model):
    patient_treatments = Model.objects.filter(event_name__category="1")
    procedure_physicians = []
    unique_physician = []
    count = 0
    count_physician = {}
    for patient in patient_treatments:
        procedures = {}
        procedures[patient.physician_id.speciality_name] = patient.physician_id.id
        procedure_physicians.append(procedures)
    for physician in procedure_physicians:
        if physician not in unique_physician:
            unique_physician.append(physician)
    for _ in unique_physician:
        for key,value in _.items():
            if key not in count_physician:
                count_physician[key] = 1
            else:
                count_physician[key] += 1
    return count_physician