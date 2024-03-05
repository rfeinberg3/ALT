# NLPFinalProject
**Abstract:**

  Hittite is one of the oldest written
languages, spoken by the ancient Hittites
with records dating as far back as the 17th
century B.C.E. in what is now modern-day
Turkey. However, the language died out
around the 13th century B.C.E and
relatively few records of the language
have been uncovered, making Hittite a low
data language. The issue is training a
language model to translate written Hittite
into written English. A difficult task for
two main reasons: as mentioned, there is a
data scarcity when it comes to labeled
Hittite to English translations. Possibly the
bigger issue though is the lack of language
models that support fine-tuning for new
languages.

## Project Overview

This project introduces an innovative approach to bridging linguistic gaps between the ancient and the modern world by translating the Hittite language into English. At the core of this endeavor lies the utilization of cutting-edge Natural Language Processing (NLP) and machine learning techniques, leveraging a transformer-based model open to the community for advancements and contributions. 
**References:**

Hittite Base Form Dictionary:
*	https://lrc.la.utexas.edu/eieol_base_form_dictionary/hitol/11

Hittite Lexicons:
*	https://www.assyrianlanguages.org/hittite/en_lexique_hittite.htm#l
* https://hittitetexts.com/en (where we get eCMD from)

Hittite To Englsh colab:
* https://colab.research.google.com/drive/1fmJe9EuumIo-uwfW4Pp3hgyz3SviomaQ?usp=sharing


No Language Left Behind GitHub:
  * https://github.com/facebookresearch/fairseq/tree/nllb
  * https://huggingface.co/facebook/nllb-200-1.3B
<--- Their Model on HuggingFace: 
  * https://github.com/facebookresearch/fairseq/blob/nllb/examples/nllb/modeling/README.md
<--- Info on fine-tuning their model:

NLLB New Language Fine-Tuning Original Example:
  * https://cointegrated.medium.com/how-to-fine-tune-a-nllb-200-model-for-translating-a-new-language-a37fc706b865
  * https://colab.research.google.com/drive/1bayEaw2fz_9Mhg9jFFZhrmDlQlBj1YZf?usp=sharing  <--- Their original colab
