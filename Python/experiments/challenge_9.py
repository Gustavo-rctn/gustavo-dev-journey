def add_urgent_patient(queue, patient_name):
    queue.insert(0, patient_name)
    return queue

emergency_room = ['Carlos', 'Ana']

new_patient = input('Enter the priority patient name: ').strip()
updated_patients = add_urgent_patient(emergency_room, new_patient)

formatted_patients = ', '.join(f'{patient}' for patient in updated_patients)

print(f'Priority patient: {new_patient}\n'
      f'Patient list (by priority order): {formatted_patients}')
