import re
xml_path = r"C:\Users\17766\Downloads\当日_ff6c39c8-a049-440b-9b11-4db2dd77680e.xml"
read_xml = open(xml_path, "r", encoding="utf8")
xml_data = read_xml.read()
entry_list = re.findall(r"<entry>(.*?)</entry>", xml_data, re.S)
for entry in entry_list:
    name = re.search(r"<name>(.*?)</name>", entry, re.S).group(1)
    vuln_id = re.search(r"<vuln-id>(.*?)</vuln-id>", entry, re.S).group(1)
    published = re.search(r"<published>(.*?)</published>", entry, re.S).group(1)
    modified = re.search(r"<modified>(.*?)</modified>", entry, re.S).group(1)
    source = re.search(r"<source>(.*?)</source>", entry, re.S).group(1)
    severity = re.search(r"<severity>(.*?)</severity>", entry, re.S).group(1)
    vuln_type = re.search(r"<vuln-type>(.*?)</vuln-type>", entry, re.S).group(1)
    vuln_descript = re.search(r"<vuln-descript>(.*?)</vuln-descript>", entry, re.S).group(1)
    cve_id = re.search(r"<cve-id>(.*?)</cve-id>", entry, re.S).group(1)
    bugtraq_id = re.search(r"<bugtraq-id>(.*?)</bugtraq-id>", entry, re.S).group(1)
    vuln_solution = re.search(r"<vuln-solution>(.*?)</vuln-solution>", entry, re.S).group(1)
    a = 1