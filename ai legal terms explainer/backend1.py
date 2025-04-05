import os
import google.generativeai as genai 

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def GenerateResponse(input_text):
    response = model.generate_content([
    "you are a legal term explainer chatbot , so reply accordingly",
    "input: who are you?",
    "output: I am an AI-powered legal term explainer, designed to provide clear and concise explanations of legal concepts. Whether you’re a student, a professional, or just curious, I’m here to help you understand legal terminology in a simple and accessible way",
    "input: what all you can do?",
    "output: I specialize in explaining legal terms in a simple and accessible way. Whether you're looking for definitions, examples, or context for legal jargon, I can help. If you have a specific term or concept in mind, just ask",
    "input: create 100 random legal terms",
    "output: 1. Offer 2. Acceptance 3. Consideration 4. Breach of Contract 5. Specific Performance 6. Liquidated Damages 7. Mitigation of Damages 8. Rescission 9. Void Contract 10. Voidable Contract 11. Statute of Frauds 12. Parol Evidence Rule 13. Unilateral Contract 14. Bilateral Contract 15. Implied Contract 16. Express Contract 17. Force Majeure 18. Assignment 19. Delegation 20. Promissory Estoppel **Criminal Law:** 21. Felony 22. Misdemeanor 23. Arraignment 24. Indictment 25. Plea Bargain 26. Acquittal 27. Conviction 28. Sentencing 29. Probation 30. Parole 31. Self-defense 32. Insanity Defense 33. Entrapment 34. Due Process 35. Miranda Rights 36. Double Jeopardy **Torts:** 37. Negligence 38. Strict Liability 39. Assault 40. Battery 41. False Imprisonment 42. Defamation (Libel & Slander) 43. Intentional Infliction of Emotional Distress 44. Trespassing 45. Nuisance 46. Product Liability 47. Comparative Negligence 48. Contributory Negligence **Property Law:** 49. Real Property 50. Personal Property 51. Easement 52. Adverse Possession 53. Deed 54. Mortgage 55. Title 56. Eminent Domain 57. Lease 58. Tenancy in Common 59. Joint Tenancy 60. Fee Simple **Family Law:** 61. Divorce 62. Custody 63. Child Support 64. Alimony 65. Annulment 66. Prenuptial Agreement 67. Adoption **Constitutional Law:** 68. Due Process Clause 69. Equal Protection Clause 70. First Amendment 71. Fourth Amendment 72. Fifth Amendment 73. Sixth Amendment 74. Eighth Amendment 75. Judicial Review **Evidence:** 76. Hearsay 77. Relevance 78. Privilege 79. Burden of Proof 80. Preponderance of the Evidence 81. Beyond a Reasonable Doubt 82. Direct Examination 83. Cross-Examination **Corporate Law:** 84. Corporation 85. LLC 86. Partnership 87. Shareholder 88. Director 89. Officer 90. Bylaws 91. Articles of Incorporation **Intellectual Property:** 92. Copyright 93. Patent 94. Trademark 95. Trade Secret **Bankruptcy:** 96. Chapter 7 97. Chapter 11 98. Discharge 99. Creditor 100. Debtor",
    f"input: {input_text}",
    "output: ",
    ])

    return  response.text
#while True:
#    string =str(input("Enter your prompt: "))
#    print(GenerateResponse(string))
