################################################################################
# Automatically-generated file. Do not edit!
################################################################################

SHELL = cmd.exe

CG_TOOL_ROOT := C:/ti/ti-cgt-arm_16.9.6.LTS

GEN_OPTS__FLAG := --cmd_file="configPkg/compiler.opt" 
GEN_CMDS__FLAG := -l"configPkg/linker.cmd" 

ORDERED_OBJS += \
"./antenna_geometry.oer4f" \
"./data_path.oer4f" \
"./main.oer4f" \
"./mmw_cli.oer4f" \
"./mmw_lvds_stream.oer4f" \
"./mmwdemo_adcconfig.oer4f" \
"./mmwdemo_flash.oer4f" \
"./mmwdemo_monitor.oer4f" \
"./mmwdemo_rfparser.oer4f" \
"./objectdetection.oer4f" \
"../mss_mmw_linker.cmd" \
"../r4f_linker.cmd" \
$(GEN_CMDS__FLAG) \
-llibosal_xwr68xx.aer4f \
-llibesm_xwr68xx.aer4f \
-llibgpio_xwr68xx.aer4f \
-llibsoc_xwr68xx.aer4f \
-llibpinmux_xwr68xx.aer4f \
-llibcrc_xwr68xx.aer4f \
-llibuart_xwr68xx.aer4f \
-llibmailbox_xwr68xx.aer4f \
-llibmmwavelink_xwr68xx.aer4f \
-llibmmwave_xwr68xx.aer4f \
-llibadcbuf_xwr68xx.aer4f \
-llibdma_xwr68xx.aer4f \
-llibedma_xwr68xx.aer4f \
-llibcli_xwr68xx.aer4f \
-llibhwa_xwr68xx.aer4f \
-llibdpm_xwr68xx.aer4f \
-llibmathutils.aer4f \
-llibcbuff_xwr68xx.aer4f \
-llibhsiheader_xwr68xx.aer4f \
-llibrangeproc_hwa_xwr68xx.aer4f \
-llibdopplerproc_hwa_xwr68xx.aer4f \
-llibcfarcaproc_hwa_xwr68xx.aer4f \
-llibaoa2dproc_hwa_xwr68xx.aer4f \
-llibstaticclutterproc_xwr68xx.aer4f \
-llibdpedma_hwa_xwr68xx.aer4f \
-llibqspi_xwr68xx.aer4f \
-llibqspiflash_xwr68xx.aer4f \
-lrtsv7R4_T_le_v3D16_eabi.lib \
-llibc.a \

-include ../makefile.init

RM := DEL /F
RMDIR := RMDIR /S/Q

# All of the sources participating in the build are defined here
-include sources.mk
-include subdir_vars.mk
-include subdir_rules.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C55_DEPS)),)
-include $(C55_DEPS)
endif
ifneq ($(strip $(C_UPPER_DEPS)),)
-include $(C_UPPER_DEPS)
endif
ifneq ($(strip $(S67_DEPS)),)
-include $(S67_DEPS)
endif
ifneq ($(strip $(S62_DEPS)),)
-include $(S62_DEPS)
endif
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(OPT_DEPS)),)
-include $(OPT_DEPS)
endif
ifneq ($(strip $(C??_DEPS)),)
-include $(C??_DEPS)
endif
ifneq ($(strip $(ASM_UPPER_DEPS)),)
-include $(ASM_UPPER_DEPS)
endif
ifneq ($(strip $(S??_DEPS)),)
-include $(S??_DEPS)
endif
ifneq ($(strip $(C64_DEPS)),)
-include $(C64_DEPS)
endif
ifneq ($(strip $(CXX_DEPS)),)
-include $(CXX_DEPS)
endif
ifneq ($(strip $(S64_DEPS)),)
-include $(S64_DEPS)
endif
ifneq ($(strip $(INO_DEPS)),)
-include $(INO_DEPS)
endif
ifneq ($(strip $(CLA_DEPS)),)
-include $(CLA_DEPS)
endif
ifneq ($(strip $(S55_DEPS)),)
-include $(S55_DEPS)
endif
ifneq ($(strip $(SV7A_DEPS)),)
-include $(SV7A_DEPS)
endif
ifneq ($(strip $(C62_DEPS)),)
-include $(C62_DEPS)
endif
ifneq ($(strip $(C67_DEPS)),)
-include $(C67_DEPS)
endif
ifneq ($(strip $(PDE_DEPS)),)
-include $(PDE_DEPS)
endif
ifneq ($(strip $(K_DEPS)),)
-include $(K_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
ifneq ($(strip $(CC_DEPS)),)
-include $(CC_DEPS)
endif
ifneq ($(strip $(C++_DEPS)),)
-include $(C++_DEPS)
endif
ifneq ($(strip $(C43_DEPS)),)
-include $(C43_DEPS)
endif
ifneq ($(strip $(S43_DEPS)),)
-include $(S43_DEPS)
endif
ifneq ($(strip $(ASM_DEPS)),)
-include $(ASM_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(CPP_DEPS)),)
-include $(CPP_DEPS)
endif
ifneq ($(strip $(SA_DEPS)),)
-include $(SA_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXE_OUTPUTS += \
out_of_box_6843_aop.xer4f \

EXE_OUTPUTS__QUOTED += \
"out_of_box_6843_aop.xer4f" \


# All Target
all: $(OBJS) $(CMD_SRCS) $(GEN_CMDS)
	@$(MAKE) --no-print-directory -Onone "out_of_box_6843_aop.xer4f"

# Tool invocations
out_of_box_6843_aop.xer4f: $(OBJS) $(CMD_SRCS) $(GEN_CMDS)
	@echo 'Building target: "$@"'
	@echo 'Invoking: Arm Linker'
	"C:/ti/ti-cgt-arm_16.9.6.LTS/bin/armcl" -mv7R4 --code_state=16 --float_support=VFPv3D16 -me -O3 --define=SOC_XWR68XX --define=SUBSYS_MSS --define=DOWNLOAD_FROM_CCS --define=MMWAVE_L3RAM_NUM_BANK=6 --define=MMWAVE_SHMEM_TCMA_NUM_BANK=0 --define=MMWAVE_SHMEM_TCMB_NUM_BANK=0 --define=MMWAVE_SHMEM_BANK_SIZE=0x20000 --define=DebugP_ASSERT_ENABLED --define=_LITTLE_ENDIAN --define=DebugP_LOG_ENABLED --define=XWR68XX_AOP_ANTENNA_PATTERN --define=USE_2D_AOA_DPU --define=AOP --define=APP_RESOURCE_FILE='<'ti/demo/xwr64xx/mmw/mmw_res.h'>' -g --diag_warning=225 --diag_wrap=off --display_error_number --gen_func_subsections=on --enum_type=int --abi=eabi --obj_extension=.oer4f -z -m"out_of_box_6843_aop.map" --heap_size=0x800 --stack_size=0x800 -i"C:/ti/ti-cgt-arm_16.9.6.LTS/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/control/mmwave/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/control/mmwavelink/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/control/dpm/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/adcbuf/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/crc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/dma/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/edma/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/esm/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/gpio/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/hwa/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/mailbox/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/osal/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/pinmux/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/soc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/uart/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/utils/cli/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/utils/mathutils/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpu/rangeproc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpc/dpu/dopplerproc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpc/dpu/cfarcaproc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpc/dpu/aoa2dproc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpc/dpu/staticclutterproc/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/datapath/dpedma/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/cbuff/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/utils/hsiheader/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/qspi/lib" -i"C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/ti/drivers/qspiflash/lib" -i"C:/ti/ti-cgt-arm_16.9.6.LTS/include" --reread_libs --disable_auto_rts --define=MMWAVE_L3RAM_NUM_BANK=6 --define=MMWAVE_SHMEM_TCMA_NUM_BANK=0 --define=MMWAVE_SHMEM_TCMB_NUM_BANK=0 --define=MMWAVE_SHMEM_BANK_SIZE=0x20000 --diag_error=10015 --diag_warning=225 --diag_wrap=off --display_error_number --warn_sections --xml_link_info="xwr64xxAOP_mmw_mss_linkInfo.xml" --rom_model --unused_section_elimination=on -o "out_of_box_6843_aop.xer4f" $(ORDERED_OBJS)
	@echo 'Finished building target: "$@"'
	@echo ' '
	@$(MAKE) --no-print-directory post-build

# Other Targets
clean:
	-$(RM) $(GEN_FILES__QUOTED)$(EXE_OUTPUTS__QUOTED)
	-$(RM) "antenna_geometry.oer4f" "data_path.oer4f" "main.oer4f" "mmw_cli.oer4f" "mmw_lvds_stream.oer4f" "mmwdemo_adcconfig.oer4f" "mmwdemo_flash.oer4f" "mmwdemo_monitor.oer4f" "mmwdemo_rfparser.oer4f" "objectdetection.oer4f" 
	-$(RM) "antenna_geometry.d" "data_path.d" "main.d" "mmw_cli.d" "mmw_lvds_stream.d" "mmwdemo_adcconfig.d" "mmwdemo_flash.d" "mmwdemo_monitor.d" "mmwdemo_rfparser.d" "objectdetection.d" 
	-$(RMDIR) $(GEN_MISC_DIRS__QUOTED)
	-@echo 'Finished clean'
	-@echo ' '

post-build:
	-C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/scripts/ImageCreator/out2rprc/out2rprc.exe out_of_box_6843_aop.xer4f out_of_box_6843_aop.tmp
	-C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/scripts/ImageCreator/multicore_image_generator/MulticoreImageGen.exe LE 37 0x00000006 out_of_box_6843_aop.bin 0x35510000 out_of_box_6843_aop.tmp 0xb5510000 C:/ti/mmwave_sdk_03_06_00_00-LTS/firmware/radarss/xwr6xxx_radarss_rprc.bin
	-C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/scripts/ImageCreator/crc_multicore_image/crc_multicore_image.exe out_of_box_6843_aop.bin out_of_box_6843_aop.tmp
	-C:/ti/mmwave_sdk_03_06_00_00-LTS/packages/scripts/ImageCreator/append_bin_crc/gen_bincrc32.exe out_of_box_6843_aop.bin
	-@echo ' '

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets

