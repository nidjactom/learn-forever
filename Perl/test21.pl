my $res;
$res=fork();

if ($res!=0)
{
print "Parent PID = $$\n";
print " Parent CPID = $res\n";
}
else
{
print "Child PID = $$\n";
}
waitpid($res,0);