#!/usr/bin/perl 

use strict;
use warnings;
use File::Copy;
use Getopt::Std;

# get the options
my %options=();
getopts("o", \%options);


my $inpreamble=1; # switch for in the preamble or not
my $filename;
my @lines=();     # @lines: stores the new lines without commands

# commands for which we want to keep the arguments- populate 
# as necessary
my %keeparguments=("textit"=>1,
                        "underline"=>1,
                        );

while (@ARGV)
{
      # get filename from arguments
      $filename = shift @ARGV; 

      # open the file
      open(INPUTFILE,$filename) or die "Can't open $filename";

      # reset the preamble switch
      $inpreamble=1;

      # reset the lines array
      @lines=();     

      # loop through the lines in the INPUT file
      while(<INPUTFILE>)
      {
          # check that the document has begun
          if($_ =~ m/\\begin{document.*/)
          {
              $inpreamble=0;   
          }
          # ignore the preamble, and make string substitutions in 
          # the main document
         if(!$inpreamble) 
         {
             # remove \begin{<stuff>}[<optional arguments>]
             s/\\begin{.*?}(\[.*?\])?({.*?})?//g;
             # remove \end{<stuff>}
             s/\\end{.*?}//g;
             # remove \<commandname>{with argument}
             while ($_ =~ m/\\(.*?){.*?}/)
             {
                if($keeparguments{$1})
                {
                  s/\\.*?{(.*?)}/$1/;
                }
                else
                {
                  s/\\.*?{.*?}//;
                }
             }
             # print the current line (if we're not overwritting the current file)
             print $_ if(!$options{o});
             push(@lines,$_);
         }
     }

     # close the file
     close(INPUTFILE);

     # if we want to over write the current file
     if ($options{o})
     {
         # make a backup of each file
         my $backupfile= "$filename.bak";
         copy($filename,$backupfile);

         # reopen the input file to overwrite it
         open(INPUTFILE,">",$filename) or die "Can't open $filename";
         print INPUTFILE @lines;
         close(INPUTFILE);

         # output to terminal
         print "Backed up original file to $filename.bak\n";
         print "Overwritten original file without commands";
     }
}

exit 
