# Ancient Language Translation (ALT) with Meta AI's No Language Left Behind (NLLB) Model

![Hittite-Cuneiform-Clay-Tablet-Writing-Language](https://github.com/rfeinberg3/Hittite_English_Translation_w-NLLB/assets/95943957/997b9af1-5404-4371-bbdf-a6bd8e2371af)


## Abstract

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

This project aims to bridge the gap between the ancient and the modern world by translating the Hittite language into English. At the core of this endeavor lies the utilization of cutting-edge Natural Language Processing (NLP) and machine learning techniques, leveraging a transformer-based model open to the community for advancements and contributions. 

### Key Features

- **Transformer-Based Model Translation:** Employs a state-of-the-art transformer-based model to understand and translate the Hittite language.

- **Custom Supervised Dataset:** Through meticulous data scraping and the development of a dataset builder tool, this project has curated a specialized dataset. This dataset features pairs of English and Hittite translations, tailored to train the translation model effectively.

- **Google Colab Integration:** The project is accessible via a Google Colab notebook for ease of use and accessibility. This notebook guides users through the process of tokenization, model fine-tuning, and evaluation, providing an interactive platform for exploring ancient Hittite translations. 

  Hittite To English colab: [https://colab.research.google.com/drive/1fmJe9EuumIo-uwfW4Pp3hgyz3SviomaQ?usp=sharing](https://colab.research.google.com/drive/1fmJe9EuumIo-uwfW4Pp3hgyz3SviomaQ?usp=sharing)

- **Performance Metrics:** To ensure the translation model's accuracy and reliability, comprehensive metrics are collected and analyzed.

  More details can be found in the report document HitToEng_Report.pdf.
The implementation at nllb_hittite_to_english_finetune.ipynb.


## Usage

**!Must run on a GPU! CPU usage is not supported!**

**Load model and tokenizer from Huggingface:**
- $ model_load_name = "ryfye181/hittite_saved_model"
- $ model = AutoModelForSeq2SeqLM.from_pretrained(model_load_name).cuda()
- $ tokenizer = NllbTokenizer.from_pretrained(model_load_name).

Using the Model for translating is demonostrated in section 8 of the Google Colab notebook.

## Metrics

### Loss over Time During Training
![image](https://github.com/rfeinberg3/Hittite_English_Translation_w-NLLB/assets/95943957/b2101ba5-36f3-4d9a-a3bf-bad2a0d06471)
### CHRF2++ Score
![image](https://github.com/rfeinberg3/Hittite_English_Translation_w-NLLB/assets/95943957/1b3e6bdf-932d-4a8c-ab49-223bde3be381)
**https://github.com/mjpost/sacrebleu#chrf--chrf**

## Translation 
Please see `Records/Nllb_Finetune_Output.csv` for an example of English to Hittite and Hittite to English translations. The `src_lang` and `tgt_lang` columns are comprised of Hittite and English words/phrases from the test set respectively. You can see the machine translations of these words on the same row in columns `hit_translated` and `eng_translated` respectively.  


## References

Hittite Base Form Dictionary:
*	https://lrc.la.utexas.edu/eieol_base_form_dictionary/hitol/11

Hittite Lexicons:
*	https://www.assyrianlanguages.org/hittite/en_lexique_hittite.htm#l
* https://hittitetexts.com/en (where we get eCMD from)


No Language Left Behind GitHub:
  * https://github.com/facebookresearch/fairseq/tree/nllb
  * https://huggingface.co/facebook/nllb-200-1.3B
<--- Their Model on HuggingFace: 
  * https://github.com/facebookresearch/fairseq/blob/nllb/examples/nllb/modeling/README.md
<--- Info on fine-tuning their model:

NLLB New Language Fine-Tuning Original Example:
  * https://cointegrated.medium.com/how-to-fine-tune-a-nllb-200-model-for-translating-a-new-language-a37fc706b865
  * https://colab.research.google.com/drive/1bayEaw2fz_9Mhg9jFFZhrmDlQlBj1YZf?usp=sharing  <--- Their original colab
