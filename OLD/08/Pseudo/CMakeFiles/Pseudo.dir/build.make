# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/shared/CMSC/165/8/Pseudo

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/shared/CMSC/165/8/Pseudo

# Include any dependencies generated for this target.
include CMakeFiles/Pseudo.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Pseudo.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Pseudo.dir/flags.make

CMakeFiles/Pseudo.dir/Pseudo.cpp.o: CMakeFiles/Pseudo.dir/flags.make
CMakeFiles/Pseudo.dir/Pseudo.cpp.o: Pseudo.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/shared/CMSC/165/8/Pseudo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/Pseudo.dir/Pseudo.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/Pseudo.dir/Pseudo.cpp.o -c /mnt/shared/CMSC/165/8/Pseudo/Pseudo.cpp

CMakeFiles/Pseudo.dir/Pseudo.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/Pseudo.dir/Pseudo.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/shared/CMSC/165/8/Pseudo/Pseudo.cpp > CMakeFiles/Pseudo.dir/Pseudo.cpp.i

CMakeFiles/Pseudo.dir/Pseudo.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/Pseudo.dir/Pseudo.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/shared/CMSC/165/8/Pseudo/Pseudo.cpp -o CMakeFiles/Pseudo.dir/Pseudo.cpp.s

CMakeFiles/Pseudo.dir/Pseudo.cpp.o.requires:

.PHONY : CMakeFiles/Pseudo.dir/Pseudo.cpp.o.requires

CMakeFiles/Pseudo.dir/Pseudo.cpp.o.provides: CMakeFiles/Pseudo.dir/Pseudo.cpp.o.requires
	$(MAKE) -f CMakeFiles/Pseudo.dir/build.make CMakeFiles/Pseudo.dir/Pseudo.cpp.o.provides.build
.PHONY : CMakeFiles/Pseudo.dir/Pseudo.cpp.o.provides

CMakeFiles/Pseudo.dir/Pseudo.cpp.o.provides.build: CMakeFiles/Pseudo.dir/Pseudo.cpp.o


# Object files for target Pseudo
Pseudo_OBJECTS = \
"CMakeFiles/Pseudo.dir/Pseudo.cpp.o"

# External object files for target Pseudo
Pseudo_EXTERNAL_OBJECTS =

Pseudo: CMakeFiles/Pseudo.dir/Pseudo.cpp.o
Pseudo: CMakeFiles/Pseudo.dir/build.make
Pseudo: /usr/local/lib/libopencv_stitching.so.3.3.0
Pseudo: /usr/local/lib/libopencv_superres.so.3.3.0
Pseudo: /usr/local/lib/libopencv_videostab.so.3.3.0
Pseudo: /usr/local/lib/libopencv_aruco.so.3.3.0
Pseudo: /usr/local/lib/libopencv_bgsegm.so.3.3.0
Pseudo: /usr/local/lib/libopencv_bioinspired.so.3.3.0
Pseudo: /usr/local/lib/libopencv_ccalib.so.3.3.0
Pseudo: /usr/local/lib/libopencv_dpm.so.3.3.0
Pseudo: /usr/local/lib/libopencv_face.so.3.3.0
Pseudo: /usr/local/lib/libopencv_freetype.so.3.3.0
Pseudo: /usr/local/lib/libopencv_fuzzy.so.3.3.0
Pseudo: /usr/local/lib/libopencv_img_hash.so.3.3.0
Pseudo: /usr/local/lib/libopencv_line_descriptor.so.3.3.0
Pseudo: /usr/local/lib/libopencv_optflow.so.3.3.0
Pseudo: /usr/local/lib/libopencv_reg.so.3.3.0
Pseudo: /usr/local/lib/libopencv_rgbd.so.3.3.0
Pseudo: /usr/local/lib/libopencv_saliency.so.3.3.0
Pseudo: /usr/local/lib/libopencv_stereo.so.3.3.0
Pseudo: /usr/local/lib/libopencv_structured_light.so.3.3.0
Pseudo: /usr/local/lib/libopencv_surface_matching.so.3.3.0
Pseudo: /usr/local/lib/libopencv_tracking.so.3.3.0
Pseudo: /usr/local/lib/libopencv_xfeatures2d.so.3.3.0
Pseudo: /usr/local/lib/libopencv_ximgproc.so.3.3.0
Pseudo: /usr/local/lib/libopencv_xobjdetect.so.3.3.0
Pseudo: /usr/local/lib/libopencv_xphoto.so.3.3.0
Pseudo: /usr/local/lib/libopencv_shape.so.3.3.0
Pseudo: /usr/local/lib/libopencv_photo.so.3.3.0
Pseudo: /usr/local/lib/libopencv_calib3d.so.3.3.0
Pseudo: /usr/local/lib/libopencv_phase_unwrapping.so.3.3.0
Pseudo: /usr/local/lib/libopencv_dnn.so.3.3.0
Pseudo: /usr/local/lib/libopencv_video.so.3.3.0
Pseudo: /usr/local/lib/libopencv_datasets.so.3.3.0
Pseudo: /usr/local/lib/libopencv_plot.so.3.3.0
Pseudo: /usr/local/lib/libopencv_text.so.3.3.0
Pseudo: /usr/local/lib/libopencv_features2d.so.3.3.0
Pseudo: /usr/local/lib/libopencv_flann.so.3.3.0
Pseudo: /usr/local/lib/libopencv_highgui.so.3.3.0
Pseudo: /usr/local/lib/libopencv_ml.so.3.3.0
Pseudo: /usr/local/lib/libopencv_videoio.so.3.3.0
Pseudo: /usr/local/lib/libopencv_imgcodecs.so.3.3.0
Pseudo: /usr/local/lib/libopencv_objdetect.so.3.3.0
Pseudo: /usr/local/lib/libopencv_imgproc.so.3.3.0
Pseudo: /usr/local/lib/libopencv_core.so.3.3.0
Pseudo: CMakeFiles/Pseudo.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/shared/CMSC/165/8/Pseudo/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable Pseudo"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Pseudo.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Pseudo.dir/build: Pseudo

.PHONY : CMakeFiles/Pseudo.dir/build

CMakeFiles/Pseudo.dir/requires: CMakeFiles/Pseudo.dir/Pseudo.cpp.o.requires

.PHONY : CMakeFiles/Pseudo.dir/requires

CMakeFiles/Pseudo.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Pseudo.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Pseudo.dir/clean

CMakeFiles/Pseudo.dir/depend:
	cd /mnt/shared/CMSC/165/8/Pseudo && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/shared/CMSC/165/8/Pseudo /mnt/shared/CMSC/165/8/Pseudo /mnt/shared/CMSC/165/8/Pseudo /mnt/shared/CMSC/165/8/Pseudo /mnt/shared/CMSC/165/8/Pseudo/CMakeFiles/Pseudo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/Pseudo.dir/depend

