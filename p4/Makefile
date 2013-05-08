CC     := gcc
CXX    := g++
LD     := g++
AR     := ar rc
RANLIB := ranlib

CXXFLAGS  := -Wall 
LDFLAGS   := -Wall 
LIBS      :=

OUTPUT += ejecutable

all: $(OUTPUT)

SRCS += main.cpp

OBJS += $(addsuffix .o,$(basename $(SRCS)))

$(OUTPUT): $(OBJS)
	$(CXX) $(LDFLAGS) -o $@ $^ $(LIBS) 

$(OUTPUTLIB): $(OBJS)
	      $(AR) $@ $(OBJS)
	      $(RANLIB) $@

clean:
	rm $(OBJS) $(OUTPUT) *~ -rf

