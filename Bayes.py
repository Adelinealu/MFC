class Bayes:
   """Initializing the parent class"""

   def __init__(self):
       """Initializing attributes of the parent class"""

   def posterior_probability(self):
       print("Paste the quiz and identify the following variables: ")
       """
       P(A) = 0.997        #prior probability
       P(B|A) = 0.001      #likelihood probability
       P(A’)  = 0.002      #prior probability prime 
       P(B|A’) = 0.999     #likelihood probability prime

       """

       self.prior_probability = float(input("Enter the prior probability: "))
       self.likelihood_probability = float(input("Enter the likelihood of evidence 'E' given the hypothesis 'H' is true: "))
       self.prior_probability_prime = float(input("Enter the reverse prior probability: "))
       self.likelihood_probability_prime = float(input("Enter the likelihood of evidence 'E' given the hypothesis 'H' is false: "))

       self.denominator = (self.prior_probability * self.likelihood_probability) + (self.likelihood_probability_prime * self.prior_probability_prime)
       self.numerator = self.prior_probability * self.likelihood_probability
       self.posterior_probability = self.numerator / self.denominator

       print(self.posterior_probability)


B = Bayes()

B.posterior_probability()
