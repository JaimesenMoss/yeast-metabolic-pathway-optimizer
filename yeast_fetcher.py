from Bio import Entrez, SeqIO
def fetch_yeast_genome(genome_id, email):
    """
    Fetches the yeast genome sequence from NCBI using the provided genome ID and email.

    Parameters:
    genome_id (str): The NCBI genome ID for the yeast genome.
    email (str): The email address to use for NCBI Entrez queries.

    
    Returns:
    str: The DNA sequence of the yeast genome.
    """
    Entrez.email = "jmoss3@calstatela.edu"
    try:
        # Fetch the genome record from NCBI
        handle = Entrez.efetch(db="nucleotide", id=genome_id, rettype="fasta", retmode="text")
        record = SeqIO.read(handle, "fasta")
        handle.close()
        return str(record.seq)
    except Exception as e:
        print(f"An error occurred while fetching the genome: {e}")
        return None
