import urllib.request
import time

start=time.time()
response = urllib.request.urlopen('https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
tld_data = response.read().decode('utf-8')

domains = []
for line in tld_data.split('\n'):
    if line and not line.startswith('#'):
        domains.append(line.strip().lower())
pass_dict = domains

with open('./urls.txt','r') as f:
    urls = f.read().splitlines()
# urls = ["https://mindsieves.com/wp1//HiNet.html:8808",
#         "https://mindsieves.com:8808"]
def cp_s(seq):
    seq = seq.split(".")
    domain_count = 0
    # print(seq[::-1])
    for url_domain in seq[::-1]:
        if url_domain in pass_dict:
            domain_count+=1
        else:
            break
    if domain_count!=0:
        if (len(seq)-domain_count)>1:
            seq = ".".join(seq[-domain_count-1::])
        else:
            seq = ".".join(seq)
    else:
        seq = ".".join(seq)
    return seq

with open('output/result_%s.csv'%(time.strftime("%m%d_%H%M", time.localtime())), 'w', encoding='utf-8-sig') as f:
    f.write("source_url, output_url\n")

    for url in urls:
        if 'http' in url:
            filter_url = url.replace('https://','').replace('http://','')
        else:
            filter_url = url
        filter_url = filter_url.split("/")
        filter_url = cp_s(filter_url[0])
        filter_url = filter_url.split(":")
        filter_url = cp_s(filter_url[0])
        filter_url = filter_url.split("?")

        f.write(f"{url},{filter_url[0]}\n")
