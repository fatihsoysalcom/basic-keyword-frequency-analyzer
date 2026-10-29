import collections
import re

def analyze_keyword_frequency(text, keywords):
    """
    Analyzes the frequency of specified keywords (single words or phrases)
    within a given text. This simulates a very basic function of an SEO
    content analysis tool, helping to understand keyword density.
    """
    text_lower = text.lower()
    results = {}

    for keyword in keywords:
        keyword_lower = keyword.lower()
        # Count non-overlapping occurrences of the exact keyword/phrase.
        # This is a simplified approach, real SEO tools are more sophisticated
        # (e.g., handling stemming, synonyms, semantic analysis).
        count = text_lower.count(keyword_lower)
        results[keyword] = count
        
    return results

if __name__ == "__main__":
    # Simulate content from a web page or blog post, similar to what an SEO tool would analyze.
    sample_content = """
    2026'da Dijital Pazarlamacıların Kullanması Gereken 15 Ücretsiz SEO Aracı.
    Dijital dünyada rekabet her geçen gün artıyor. Markanızın görünürlüğünü artırmak ve
    potansiyel müşterilere ulaşmak için SEO (Arama Motoru Optimizasyonu) artık bir lüks değil,
    bir zorunluluk. Peki, bütçeniz kısıtlıysa veya yeni başlıyorsanız, bu karmaşık dünyada
    hangi araçları kullanmalısınız? İşte 2026 yılında her dijital pazarlamacının mutlaka
    bilmesi ve kullanması gereken, birbirinden faydalı 15 ücretsiz SEO aracı...

    Bu makalede, başlangıç seviyesinden ileri seviyeye kadar her türden dijital pazarlamacının
    işini kolaylaştıracak, markanızın arama motorlarındaki sıralamasını yükseltmenize yardımcı
    olacak araçları inceleyeceğiz. Kimi anahtar kelime araştırması için, kimi site içi teknik
    analizler için, kimi de rakip analizi için biçilmiş kaftan. Önemli olan, bu araçları doğru
    stratejilerle birleştirerek maksimum verimi alabilmek. Gelin, bu yolculuğa birlikte çıkalım
    ve dijital pazarlamanın olmazsa olmazlarını keşfedelim.

    Neden Ücretsiz SEO Araçları Önemli?
    Profesyonel SEO araçları genellikle yüksek maliyetli olabilir. Ancak dijital pazarlama
    dünyası sürekli gelişiyor ve artık birçok güçlü araç ücretsiz olarak da kullanıcılara
    sunuluyor. Bu durum, özellikle küçük işletmeler, yeni girişimler veya kısıtlı bütçeyle
    çalışan pazarlamacılar için büyük bir avantaj.
    """

    # Keywords a digital marketer might want to track for their content.
    # These are examples of keywords that free SEO tools help analyze.
    target_keywords = ["SEO", "dijital pazarlama", "araçlar", "ücretsiz", "anahtar kelime", "pazarlamacı"]

    print("--- SEO Keyword Frequency Analyzer ---")
    print(f"Analyzing content for keywords: {', '.join(target_keywords)}\n")

    # Perform the analysis, simulating a feature of an SEO content analysis tool.
    keyword_frequencies = analyze_keyword_frequency(sample_content, target_keywords)

    print("Keyword Frequencies:")
    for keyword, count in keyword_frequencies.items():
        # This output directly illustrates how SEO tools help identify keyword usage.
        print(f"  '{keyword}': {count} occurrences")

    print("\n--- Analysis Complete ---")
