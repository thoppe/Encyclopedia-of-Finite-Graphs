all:
	echo "Makefile is only for compiling the src"
	echo "Use fabic [fab --list]"

# Must be called first
compile:
	pip install -r requirements.txt
	(cd EoGF/invariants/bliss && make -j gmp)
	(cd EoGF/invariants/independent_edge_sets && make -j)
	(cd EoGF/invariants/independent_vertex_sets && make -j)
	(cd EoGF/nauty/ && ./configure && make -j)

clean:
	(cd EoGF/invariants/bliss && make clean)
	(cd EoGF/invariants/independent_edge_sets && make clean)
	(cd EoGF/invariants/independent_vertex_sets && make clean)
	(cd EoGF/nauty/ && make clean)

#report_lvl1:
#	python verification/lvl1_report.py > verification/raw_lvl1.md

#sequence:
#	python EoGF/build_sequence.py --max_n $(max_n)
#	python EoGF/build_relations.py --max_n $(max_n)
#	python verification/raw_dump_relations.py 
