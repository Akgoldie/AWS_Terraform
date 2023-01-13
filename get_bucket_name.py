
def get_bucket_name(repository_name):   #Create Function
    repository_text_list = repository_name.split("-")   #Split(-) the string store in repository_text_list
    bucket_name = "-".join(repository_text_list[:4])    #join(-) the strings store in bucket_name
    return bucket_name      #return bucket_name


repository_name = "arun-is-a-good-bad-boy"  #input
print(get_bucket_name(repository_name))     #call the function
