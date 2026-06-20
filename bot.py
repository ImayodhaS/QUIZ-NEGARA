import discord
from discord.ext import commands
import logic 
from config import TOKEN

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

kuis_berjalan = {}

@bot.event
async def on_ready():
    print(f"Bot Kuis Terdaftar (10 Poin) {bot.user} sudah online!")



@bot.command()
async def kuis(ctx, nama_pemain: str = None):
    """Cara jalankan: !kuis [NamaOrang]"""
    if nama_pemain is None:
        await ctx.send("Silahkan masukkan nama pemain! Contoh: `!kuis Made`")
        return
        
    soal = logic.ambil_soal_acak()
    
    kuis_berjalan[ctx.channel.id] = {
        "soal": soal,
        "pemain": nama_pemain
    }
    
    opsi_teks = "\n".join([f"• {p}" for p in soal["pilihan"]])
    
    embed = discord.Embed(
        title="Quiz DUnia",
        description=f"**Pemain Saat Ini:** {nama_pemain}\n\n**Pertanyaan:**\n{soal['pertanyaan']}\n\n**Pilihan Jawaban:**\n{opsi_teks}",
        color=0x3498db
    )
    embed.set_footer(text=f"Ketik: !jawab [Jawaban] untuk menambah 10 poin {nama_pemain}")
    await ctx.send(embed=embed)

@bot.command()
async def jawab(ctx, *, argumen_jawaban: str):
    channel_id = ctx.channel.id
    
    if channel_id not in kuis_berjalan:
        await ctx.send("Belum ada kuis yang berjalan. Ketik `!kuis [Nama]` dulu!")
        return
        
    data_aktif = kuis_berjalan[channel_id]
    soal = data_aktif["soal"]
    nama_terdaftar = data_aktif["pemain"]
    
    apakah_benar = logic.periksa_jawaban(soal, argumen_jawaban)
    
    if apakah_benar:
        skor_terbaru = logic.tambah_skor(nama_terdaftar)
        
        await ctx.send(f"**BENAR**! Jawabannya adalah **{soal['benar']}**.\n Poin untuk **{nama_terdaftar}** bertambah! Total: **{skor_terbaru} Poin**.")
        del kuis_berjalan[channel_id]
    else:
        await ctx.send(f"Yah, jawaban untuk sesi kuis **{nama_terdaftar}** masih salah. Ayo coba tebak lagi!")

@bot.command()
async def skor(ctx):
    """Melihat papan poin total dari para pemain"""
    if not logic.skor_pemain:
        await ctx.send("Belum ada poin yang tercatat dari para pemain.")
        return
        
    papan_skor = ""
    nomor = 1

    for nama, poin in sorted(logic.skor_pemain.items(), key=lambda item: item[1], reverse=True):
        papan_skor += f"{nomor}. **{nama}** — {poin} Poin\n"
        nomor += 1
        
    embed = discord.Embed(
        title=" PAPAN POIN PEMAIN KUIS ",
        description=papan_skor,
        color=0xf1c40f
    )
    await ctx.send(embed=embed)


bot.run(TOKEN)