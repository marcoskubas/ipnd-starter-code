import csv
def read_csv(filename):
	with open(filename, 'rb') as f:
		reader = csv.DictReader(f)
		return list(reader)

enrollments         = read_csv('enrollments.csv')
#daily_engagement    = read_csv('daily_engagement.csv')
#project_submissions = read_csv('project_submissions.csv')

print enrollments[0]