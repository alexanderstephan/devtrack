cmake_minimum_required(VERSION 3.15)
project(newFrontend)

set(CMAKE_CXX_STANDARD 17)

add_executable(newFrontend main.cpp)

target_link_libraries(newFrontend ncurses)