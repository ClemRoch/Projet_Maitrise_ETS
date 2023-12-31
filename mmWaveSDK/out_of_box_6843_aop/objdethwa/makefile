###################################################################################
#   objdethwa Test makefile
###################################################################################
# The following needs to be before any makefile inclusion
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MODULE_NAME := $(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))

include $(MMWAVE_SDK_INSTALL_PATH)/ti/common/mmwave_sdk.mak

##################################################################################
# SOC Specific Test Targets
##################################################################################
ifneq ($(filter $(MMWAVE_SDK_DEVICE_TYPE), xwr68xx xwr18xx), )
include ./test/mssTest.mak
include ./test/dssTest.mak
###################################################################################
# Standard Targets which need to be implemented by each mmWave SDK module. This
# plugs into the release scripts.
###################################################################################
.PHONY: all clean test testClean mssTest mssTestClean dssTest dssTestClean help


# Clean: This cleans all the objects
clean:      testClean

# This will build the hwa_edma test
all: test


ifeq ($(MMWAVE_SDK_DEVICE_TYPE),xwr18xx)
test:
	$(MAKE) -s mssTest
	$(MAKE) -s dssTest
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP mssTest
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP dssTest

testClean:
	$(MAKE) -s mssTestClean
	$(MAKE) -s dssTestClean
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP mssTestClean
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP dssTestClean
endif

ifeq ($(MMWAVE_SDK_DEVICE_TYPE),xwr68xx)
test:
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP mssTest
	$(MAKE) -s mssTest
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP dssTest
	$(MAKE) -s dssTest

testClean:
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP mssTestClean
	$(MAKE) -s mssTestClean
	$(MAKE) -s MMWAVE_SDK_LIB_BUILD_OPTION=AOP dssTestClean
	$(MAKE) -s dssTestClean
endif    

# Help: This displays the MAKEFILE Usage.
help:
	@echo '****************************************************************************************'
	@echo '* Makefile Targets for the objdethwa test '
	@echo 'clean             -> Clean out all the objects'
	@echo 'test              -> Builds all the unit tests for the module'
	@echo 'testClean         -> Cleans all the Unit Tests for the module'
	@echo '****************************************************************************************'

else
# For some reason the .DEFAULT does not seem to work for lib, test
.PHONY: lib test

lib test .DEFAULT:
	@echo "Error: $(MODULE_NAME) is not supported on $(MMWAVE_SDK_DEVICE) !!!"
endif

