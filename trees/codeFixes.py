applications = []
application_index = set()

''' To fix: Returns duplicates'''
def submit_application(candidate_id, job_id):
    key = (candidate_id, job_id) # key=["alice", "eng-101"]
    print(key)
    
    if key in application_index: 
        raise ValueError("Duplicate application")

    application = {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "status": "applied" 
    }

    applications.append(application) # [{"candidate_id": alice, "job_id": eng-101, "status": "applied"}, {...}] 
    application_index.add(key) # [["alice", "eng-101"], [...]]
    return application


result1 = submit_application("alice", "eng-101")
print(result1)  # Should return a valid application dict

result2 = submit_application("alice", "eng-101")
# result3 = submit_application("alice", "eng-101")  # Should raise ValueError
print(result2)
# print(result3)