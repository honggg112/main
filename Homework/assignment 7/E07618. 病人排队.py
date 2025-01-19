def patient_registration():
    # 读取病人个数
    n = int(input())
    patients = []

    # 收集每个病人的信息
    for _ in range(n):
        patient_info = input().split()
        patient_id = patient_info[0]
        age = int(patient_info[1])
        patients.append((patient_id, age))

    # 分开老年人和非老年人
    old_patients = []
    young_patients = []

    for patient in patients:
        if patient[1] >= 60:
            old_patients.append(patient)
        else:
            young_patients.append(patient)

    old_patients.sort(key=lambda x: -x[1])

    # 合并排序好的老年人和非老年人
    sorted_patients = old_patients + young_patients

    # 输出排序后的病人ID
    for patient in sorted_patients:
        print(patient[0])
# 运行函数
patient_registration()