def getprofile(request):
    from_dict = {'aboutme': 'aboutme.png',
                 'techskills': 'tech_skills.png',
                 'education': 'education.png',
                 'experience': 'experience.png'}
    return from_dict[request.GET['from']]