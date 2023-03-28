# Project SnowLynx
FAQ is below, enjoy your stay :)

![projectSnowLynx](https://user-images.githubusercontent.com/116419257/227973320-b3a2791e-301d-4b3c-b59a-4fc27b6c77a0.jpg)


# FAQ
### What is Project SnowLynx?
Project SnowLynx(PSL) is currently a Raspberry Pi Pico based Flight Control system aimed to provide modes for 3-axis stabilization, data logging, flight control surface blending, and more.

### Why Project SnowLynx? Why are you not commercially available 3-axis gyros?
Well, for one, why not?

I got bored in my Latin Class, and started browsing options for R/C Aircraft systems. I found many were available, only at steep prices(or in other cases with affordable options, like the Omnibus F4, theres no stock).
	
I'm a maker, why not make it myself? And so I will! The ability to specifically tailor this FCS to my aircraft and model the FCS to operate it as best as it can is something only custom projects could provide. Consumer Flight Controllers are great, and certainly don't let me discourage you from buying one(<sub>as if I was discouraging anyone to begin with</sub>). This is simply a project to build my skills as a budding Aerospace Engineer and make my R/C aircraft the best aircraft available.

### What does this require?
I don't know why you would want to follow me off a cliff here, but if so, heres the deal:

Electronics, soldering iron, all that, but most importantly:
***Time.***

More to the elctronics bit, heres the Bill of Materials so far(this includes base components for the R/C airplane):
- Raspberry Pi Pico
- Silicone-wrapped wire(22AWG should be fine)
- Servos(cheap 9g are fine, don't go above ~6 servos without more amps on the BEC. 5v from the USB **will not** power more than 2 servos alone.)
- Servo Extensions(For ease of unplugging servos, and more importantly soldering connectors to the board)
- 50uF Capacitor
- 100uF Capacitor
- ESCs, with BEC 5v at 5A is recommended
- **Minimum** 4ch reciever(Rx). SBUS is not currently supported. 
- Probably LEDs of some sort, a more accurate list will follow later.

### Are you even qualified? Who even are you?
Great question! I often ask that myself

The answer is no, not explicitly qualified. But I am certainly motivated. I can code, I can fly, and I can combine the two. 

I am in High School and pursuing a career path in Aerospace Engineering or Computer Science, all of which is based on my hobbies and general interest. 

### What pace are you going at? How soon will this be ready to fly?
Ideally first static tests of the stability system by mid-April 2023. Passive carry by early to mid April as well. I will know more by then.

There is not any specific pace at all, but the sooner it is up the sooner I'm happy. Ideally by mid to late May I'd like to have the first major release.

### What the h*ck is this release system???
Alphas, Betas, and releases.

Alphas are incredibly minor bug fixes and/or software building and are often majorly borked. I will sometimes use this just to save the project for a second so I can work on it elsewhere.

Betas are functional, but not polished. Think passive flight or static tests, these will be Betas. 

Fully fledged releases are working and functional with little to no bugs(I'm kidding, no bugs is impossible). 

There will be Alphas in between Betas and such, it is about the state of the software more than the lineage of release.

Epsilons are special releases intent on experimental flight testing. I will not provide much more information outside of the code and what it's purpose is. Yes I used Epsilon because it's Greek, consistency baby 

Versions will be notated with "Stable" if I deem them functional enough. This mostly applies to Betas as Alphas will almost never get to this point and full releases are inherently Stable.

Betas and Releases have requirements that must be met before the Beta is released. This may include polishing, optimization, or functions. Alphas have no requirements.

## Other things to mention
I honestly have no idea why I'm putting this on GitHub, but it's code and it's a code website. It's not illegal, just 99% pointless. 
