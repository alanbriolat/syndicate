==============
Data Structure
==============

Syndicating data from several different sources requires data to be cached in a source-specific way.  
We cannot hope to create a general format that would encompass every possible thing from every 
possible source.

Let's use an ugly but effective approach.  We have a database where we cache the data.  Each source 
has one or more tables containing event data (and possibly others containing related data).  Each 
fetcher can deal with this in its own way.  Extracting information like "all activity since a 
particular datetime" is easy, if tedious, in this format.  However what we probably want is to 
extract "the most recent ``n`` things" instead.  So let's create an "event stream" table which 
consists only of timestamps, table references and identifier references.  This is the bare minimum 
amount of data required to work on the dataset as a whole.  This way chunks can be selected (and 
later expanded) independent of source, and even filtered based on the table identifier (a.k.a. event 
type).
