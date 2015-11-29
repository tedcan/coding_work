#!/bin/bash

python ModifiedPageRank/PageRank.py < ModifiedPageRank/InputFiles/finalGraph.txt > ModifiedPageRank/IntermediateFiles/OutputFile1.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile1.txt > ModifiedPageRank/IntermediateFiles/OutputFile2.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile2.txt > ModifiedPageRank/IntermediateFiles/OutputFile3.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile3.txt > ModifiedPageRank/IntermediateFiles/OutputFile4.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile4.txt > ModifiedPageRank/IntermediateFiles/OutputFile5.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile5.txt > ModifiedPageRank/IntermediateFiles/OutputFile6.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile6.txt > ModifiedPageRank/IntermediateFiles/OutputFile7.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile7.txt > ModifiedPageRank/IntermediateFiles/OutputFile8.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile8.txt > ModifiedPageRank/IntermediateFiles/OutputFile9.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile9.txt > ModifiedPageRank/IntermediateFiles/OutputFile10.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile10.txt > ModifiedPageRank/IntermediateFiles/OutputFile11.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile11.txt > ModifiedPageRank/IntermediateFiles/OutputFile12.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile12.txt > ModifiedPageRank/IntermediateFiles/OutputFile13.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile13.txt > ModifiedPageRank/IntermediateFiles/OutputFile14.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile14.txt > ModifiedPageRank/IntermediateFiles/OutputFile15.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile15.txt > ModifiedPageRank/IntermediateFiles/OutputFile16.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile16.txt > ModifiedPageRank/IntermediateFiles/OutputFile17.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile17.txt > ModifiedPageRank/IntermediateFiles/OutputFile18.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile18.txt > ModifiedPageRank/IntermediateFiles/OutputFile19.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile19.txt > ModifiedPageRank/IntermediateFiles/OutputFile20.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile20.txt > ModifiedPageRank/IntermediateFiles/OutputFile21.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile21.txt > ModifiedPageRank/IntermediateFiles/OutputFile22.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile22.txt > ModifiedPageRank/IntermediateFiles/OutputFile23.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile23.txt > ModifiedPageRank/IntermediateFiles/OutputFile24.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile24.txt > ModifiedPageRank/IntermediateFiles/OutputFile25.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile25.txt > ModifiedPageRank/IntermediateFiles/OutputFile26.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile26.txt > ModifiedPageRank/IntermediateFiles/OutputFile27.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile27.txt > ModifiedPageRank/IntermediateFiles/OutputFile28.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile28.txt > ModifiedPageRank/IntermediateFiles/OutputFile29.txt
python ModifiedPageRank/PageRank.py < ModifiedPageRank/IntermediateFiles/OutputFile29.txt > ModifiedPageRank/OutputFiles/FinalOutputFile.txt

rm ModifiedPageRank/IntermediateFiles/OutputFile1.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile2.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile3.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile4.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile5.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile6.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile7.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile8.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile9.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile10.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile11.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile12.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile13.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile14.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile15.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile16.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile17.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile18.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile19.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile20.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile21.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile22.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile23.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile24.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile25.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile26.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile27.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile28.txt
rm ModifiedPageRank/IntermediateFiles/OutputFile29.txt

python ModifiedPageRank/SortOutput.py
