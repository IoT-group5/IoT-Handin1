TARGETS = \
	Logger.class \
	OutputLogger.class \
	ProcessLogger.class \
	TestHarness.class \

LOGS = \
	siggenlog_output.log \
	siggenlog_process.log \
	mavglog_output.log \
	mavglog_process.log \
	funclog_output.log \
	funclog_process.log \
	clientlog_output.log \
	clientlog_process.log \	

CP = -classpath ".:javasysmon-0.3.5.1.jar"

all: ${TARGETS}

clean:
	touch ${TARGETS}
	rm    ${TARGETS}
	
purgelogs:
	touch ${LOGS}
	rm    ${LOGS}

mrproper: clean
	touch d~
	rm    *~

deps:
	echo Download from https://jar-download.com/artifact-search/javasysmon and extract jar file here. Code expects the result to be named "javasysmon-0.3.5.1.jar".


Logger.class: Logger.java
	javac Logger.java

OutputLogger.class: OutputLogger.java
	javac OutputLogger.java

ProcessLogger.class: ProcessLogger.java
	javac ${CP} ProcessLogger.java

TestHarness.class: TestHarness.java
	javac ${CP} TestHarness.java

TestHarness: ${TARGETS}
	java ${CP} TestHarness run42 chromium-browser

#Our make commands

TestHarnessSiggen: ${TARGETS}
	java ${CP} TestHarness siggenlog go run ../siggen/mqtt-siggen.go
	
TestHarnessMavg: ${TARGETS}
	java ${CP} TestHarness mavglog go run ../mavg/mqtt-mavg.go
	
TestHarnessFunc: ${TARGETS}
	java ${CP} TestHarness funclog go run ../func/mqtt-func.go
	
TestHarnessClient: ${TARGETS}
	java ${CP} TestHarness clientlog mosquitto_sub -v -t "func/+/+"
	
