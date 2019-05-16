function FindProxyForURL(url, host)
{
if ((isPlainHostName(host) 
|| dnsDomainIs(host, ".iitg.ac.in")) 
&& !localHostOrDomainIs(host, ".iitg.ernet.in") 
&& isInNet(host, "202.141.80.1", "255.255.0.0"))
return "DIRECT";
else return "PROXY 202.141.80.80:3128";
}
