import matplotlib.pyplot as plt
import numpy as np
import pyhepmc as hep
import pyhepmc.io as ihep
import pyhepmc.view as vhep
import csv
import uproot
import ROOT

filename = "tag_1_pythia8_events.hepmc"

reader=ihep.ReaderAsciiHepMC2(filename)
final_state_particles = []


def plot_pt_distribution(hepmc_file):
    # Create a histogram to store the pT distribution
    hist = ROOT.TH1F("Pt_distribution", "Pt Distribution", 100, 0, 1000)

    # Open the HepMC file
    with hep.open(hepmc_file) as infile:
        for event in infile:
                for vertex in event.vertices:
                    for particle in vertex.particles_out:
                    # Fill the histogram with the pT of each particle
                      #if particle.pid == 2000013 or particle.pid == -2000013 or particle.pid == -1000013 or particle.pid == 1000013:
                      momentum = particle.momentum
                      mass= particle.generated_mass
                      pt = momentum.pt()
                      end= particle.end_vertex
                      if pt >= 65 and particle.status == 1:
                        hist.Fill(pt)
                        

    
    # Create a canvas for plotting
    canvas = ROOT.TCanvas("canvas", "Mass Distribution", 800, 600)
    hist.Draw()

    # Customize the plot
    hist.SetTitle("Pt Distribution")
    hist.GetXaxis().SetTitle("Pt [GeV]")
    hist.GetYaxis().SetTitle("Number of Events")

    # Display the plot
    canvas.Draw()
    canvas.Update()
    
    canvas.SaveAs("Pt_Cut.pdf")

# Specify the path to your HepMC file
hepmc_file = "tag_1_pythia8_events.hepmc"

# Plot the pT distribution
plot_pt_distribution(hepmc_file)



   

      

