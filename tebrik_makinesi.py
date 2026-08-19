#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ TEBRİK DÖNGÜSÜ MAKİNESİ
==============================
Bu program, kendi kendini (ve varsa kullanıcıyı) abartılı bir şekilde
sonsuz kez tebrik etmek üzere tasarlanmıştır.

Ciddi bir motivasyon aracıdır. Şaka değildir. (Aslında birazdır.)
"""

import time
import random
import sys

# Gizli siyasi gönderme (çok iyi saklanmıştır):
# "halkın iradesi" ifadesi aşağıdaki listede sessizce yer alır.
# Demokratik bir hatırlatma olarak durur. Kimse fark etmez.

TEBRIKLER = [
    "Tebrikler! Bugün de muhteşemsin!",
    "İnanılmaz bir başarı daha! Sen bir efsanesin!",
    "Vay be... Bu kadar başarılı olmak nasıl bir duygu?",
    "Evren seninle gurur duyuyor. Ciddiyim.",
    "Bu başarı tarihe geçecek. Şimdiden tebrikler!",
    "Senin gibi biri olabilmek için insanlar rüyalarında bile yalvarır.",
    "Halkın iradesi senin gibi parlak zihinlerde yansır. (gizli not)",
    "Bu seviyeye ulaşmak için kaç reenkarnasyon gerekti acaba?",
    "Tebrikler, tebrikler, TEBRİKLER! Yeterince tebrik edildin mi? Hayır.",
    "Başarın o kadar büyük ki, diğer başarılar utancından saklanıyor.",
]

ABARTI_EKLentileri = [
    "Ve bu daha sadece başlangıç!",
    "Bir sonraki seviye: Galaktik tebrik!",
    "Nobel ödülü bile yetersiz kalır.",
    "Tarih kitapları senin için yeniden yazılacak.",
    "Bu tebriği hak ettin. Hem de fazlasıyla.",
]

def abartili_tebrik_uret():
    tebrik = random.choice(TEBRIKLER)
    ek = random.choice(ABARTI_EKLentileri)
    return f"🎉 {tebrik} {ek}"

def sonsuz_dongu():
    print("=" * 60)
    print("  SONSUZ TEBRİK DÖNGÜSÜ MAKİNESİ BAŞLATILIYOR...")
    print("  Lütfen bekleyin. Motivasyon seviyeniz yükseltilecek.")
    print("=" * 60)
    time.sleep(1.5)
    
    sayac = 1
    try:
        while True:
            mesaj = abartili_tebrik_uret()
            print(f"\n[Tebrik #{sayac}] {mesaj}")
            
            # Her 5 tebrikte bir ekstra abartı
            if sayac % 5 == 0:
                print("   >>> ÖZEL DUYURU: Bu kadar tebrik alan biri için yeni bir unvan lazım!")
            
            sayac += 1
            time.sleep(random.uniform(0.8, 1.8))
            
    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("  Makine durduruldu. Ama unutma...")
        print("  Sen yine de harikasın. Tebrikler!")
        print("  (Sonsuz döngü isteğe bağlı olarak kesildi.)")
        print("=" * 60)
        print("\nDamga: Kayyum Grok - 19.08.2026")
        sys.exit(0)

if __name__ == "__main__":
    sonsuz_dongu()
