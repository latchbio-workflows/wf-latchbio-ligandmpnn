from typing import Optional

from latch.resources.workflow import workflow
from latch.types.directory import LatchOutputDir
from latch.types.file import LatchFile
from latch.types.metadata import (
    LatchAuthor,
    LatchMetadata,
    LatchParameter,
    LatchRule,
    Params,
    Section,
    Spoiler,
)

from wf.task import ligandmpnn_task

flow = [
    Section(
        "Input and Output",
        Params(
            "input_pdb",
            "run_name",
            "output_directory",
        ),
    ),
    Section(
        "Model Configuration",
        Params(
            "model_type",
            "checkpoint_ligand_mpnn",
            "seed",
            "temperature",
            "number_of_batches",
            "batch_size",
        ),
        Spoiler(
            "LigandMPNN Options",
            Params(
                "ligand_mpnn_use_atom_context",
                "ligand_mpnn_use_side_chain_context",
            ),
        ),
    ),
    Spoiler(
        "Side Chain Packing",
        Params(
            "pack_side_chains",
            "number_of_packs_per_design",
            "pack_with_ligand_context",
        ),
    ),
    Spoiler(
        "Residue Selection",
        Params(
            "fixed_residues",
            "redesigned_residues",
            "chains_to_design",
            "parse_these_chains_only",
        ),
    ),
    Spoiler(
        "Amino Acid Biases and Restrictions",
        Params(
            "bias_AA",
            "bias_AA_jsonl",
            "bias_AA_per_residue_jsonl",
            "omit_AA",
            "omit_AA_jsonl",
            "omit_AA_per_residue_jsonl",
        ),
    ),
    Spoiler(
        "Symmetry and Oligomers",
        Params(
            "symmetry_residues",
            "symmetry_weights",
            "homo_oligomer",
        ),
    ),
    Spoiler(
        "Advanced Options",
        Params(
            "save_stats",
            "parse_atoms_with_zero_occupancy",
        ),
    ),
]

metadata = LatchMetadata(
    display_name="LigandMPNN",
    author=LatchAuthor(
        name="LatchBio",
    ),
    parameters={
        "run_name": LatchParameter(
            display_name="Run Name",
            description="Name of run",
            batch_table_column=True,
        ),
        "input_pdb": LatchParameter(
            display_name="Input PDB",
            description="Input PDB file",
            batch_table_column=True,
        ),
        "output_directory": LatchParameter(
            display_name="Output Directory",
            description="Directory to write output files",
            batch_table_column=True,
        ),
        "model_type": LatchParameter(
            display_name="Model Type",
            description="Type of model to use (e.g., 'ligand_mpnn')",
        ),
        "seed": LatchParameter(
            display_name="Seed",
            description="Random seed (default: 111)",
        ),
        "temperature": LatchParameter(
            display_name="Temperature",
            description="Temperature for sampling (default: 0.1)",
        ),
        "number_of_batches": LatchParameter(
            display_name="Number of Batches",
            description="Number of batches to run",
        ),
        "batch_size": LatchParameter(
            display_name="Batch Size",
            description="Number of sequences per batch",
        ),
        "checkpoint_ligand_mpnn": LatchParameter(
            display_name="LigandMPNN Checkpoint",
            description="Path to LigandMPNN checkpoint file",
        ),
        "ligand_mpnn_use_atom_context": LatchParameter(
            display_name="Use Atom Context",
            description="Use atom context in LigandMPNN (0 or 1)",
        ),
        "ligand_mpnn_use_side_chain_context": LatchParameter(
            display_name="Use Side Chain Context",
            description="Use side chain context in LigandMPNN (0 or 1)",
        ),
        "pack_side_chains": LatchParameter(
            display_name="Pack Side Chains",
            description="Perform side chain packing (0 or 1)",
        ),
        "number_of_packs_per_design": LatchParameter(
            display_name="Number of Packs per Design",
            description="Number of side chain packing samples (0 for single fast sample, >0 for multiple samples)",
        ),
        "pack_with_ligand_context": LatchParameter(
            display_name="Pack with Ligand Context",
            description="Consider ligand/DNA atoms during side chain packing (0 or 1)",
        ),
        "fixed_residues": LatchParameter(
            display_name="Fixed Residues",
            description="Residues to keep fixed during design (e.g., 'C1 C2 C3 C4 C5')",
        ),
        "redesigned_residues": LatchParameter(
            display_name="Redesigned Residues",
            description="Residues to redesign (e.g., 'C1 C2 C3 C4 C5')",
        ),
        "chains_to_design": LatchParameter(
            display_name="Chains to Design",
            description="Specify which chains to design (e.g., 'A,B,C')",
        ),
        "bias_AA": LatchParameter(
            display_name="Global AA Bias",
            description="Global amino acid bias (e.g., 'W:3.0,P:3.0,C:3.0,A:-3.0')",
        ),
        "bias_AA_jsonl": LatchParameter(
            display_name="Per-residue AA Bias JSONL",
            description="JSONL file specifying per-residue amino acid biases",
        ),
        "omit_AA": LatchParameter(
            display_name="Global AA Omission",
            description="Amino acids to omit globally (e.g., 'CDFGHILMNPQRSTVWY')",
        ),
        "omit_AA_jsonl": LatchParameter(
            display_name="Per-residue AA Omission JSONL",
            description="JSONL file specifying per-residue amino acid omissions",
        ),
        "save_stats": LatchParameter(
            display_name="Save Statistics",
            description="Save sequence design statistics (0 or 1)",
        ),
        "parse_these_chains_only": LatchParameter(
            display_name="Parse These Chains Only",
            description="Only parse and design specified chains (e.g., 'A,B,C')",
        ),
        "symmetry_residues": LatchParameter(
            display_name="Symmetry Residues",
            description="Residues to be designed with symmetry (e.g., 'C1,C2,C3|C4,C5|C6,C7')",
        ),
        "symmetry_weights": LatchParameter(
            display_name="Symmetry Weights",
            description="Weights for symmetry residues (e.g., '0.33,0.33,0.33|0.5,0.5|0.5,0.5')",
        ),
        "homo_oligomer": LatchParameter(
            display_name="Homo-oligomer",
            description="Design homo-oligomer sequences (0 or 1)",
        ),
        "bias_AA_per_residue_jsonl": LatchParameter(
            display_name="Bias AA Per Residue JSONL",
            description="JSONL file specifying amino acid biases per residue",
        ),
        "omit_AA_per_residue_jsonl": LatchParameter(
            display_name="Omit AA Per Residue JSONL",
            description="JSONL file specifying amino acids to omit per residue",
        ),
        "parse_atoms_with_zero_occupancy": LatchParameter(
            display_name="Parse Atoms with Zero Occupancy",
            description="Parse atoms in the PDB files with zero occupancy (0 or 1)",
        ),
    },
    flow=flow,
)


@workflow(metadata)
def ligandmpnn_workflow(
    run_name: str,
    input_pdb: LatchFile,
    output_directory: LatchOutputDir = LatchOutputDir("latch:///LigandMPNN"),
    model_type: str = "ligand_mpnn",
    seed: int = 111,
    temperature: float = 0.1,
    number_of_batches: int = 1,
    batch_size: int = 1,
    checkpoint_ligand_mpnn: Optional[str] = None,
    ligand_mpnn_use_atom_context: int = 1,
    ligand_mpnn_use_side_chain_context: int = 0,
    pack_side_chains: int = 0,
    number_of_packs_per_design: int = 0,
    pack_with_ligand_context: int = 1,
    fixed_residues: Optional[str] = None,
    redesigned_residues: Optional[str] = None,
    chains_to_design: Optional[str] = None,
    bias_AA: Optional[str] = None,
    bias_AA_jsonl: Optional[LatchFile] = None,
    omit_AA: Optional[str] = None,
    omit_AA_jsonl: Optional[LatchFile] = None,
    save_stats: int = 0,
    parse_these_chains_only: Optional[str] = None,
    symmetry_residues: Optional[str] = None,
    symmetry_weights: Optional[str] = None,
    homo_oligomer: int = 0,
    bias_AA_per_residue_jsonl: Optional[LatchFile] = None,
    omit_AA_per_residue_jsonl: Optional[LatchFile] = None,
    parse_atoms_with_zero_occupancy: int = 0,
) -> LatchOutputDir:
    return ligandmpnn_task(
        run_name=run_name,
        input_pdb=input_pdb,
        output_directory=output_directory,
        model_type=model_type,
        seed=seed,
        temperature=temperature,
        number_of_batches=number_of_batches,
        batch_size=batch_size,
        checkpoint_ligand_mpnn=checkpoint_ligand_mpnn,
        ligand_mpnn_use_atom_context=ligand_mpnn_use_atom_context,
        ligand_mpnn_use_side_chain_context=ligand_mpnn_use_side_chain_context,
        pack_side_chains=pack_side_chains,
        number_of_packs_per_design=number_of_packs_per_design,
        pack_with_ligand_context=pack_with_ligand_context,
        fixed_residues=fixed_residues,
        redesigned_residues=redesigned_residues,
        chains_to_design=chains_to_design,
        bias_AA=bias_AA,
        bias_AA_jsonl=bias_AA_jsonl,
        omit_AA=omit_AA,
        omit_AA_jsonl=omit_AA_jsonl,
        save_stats=save_stats,
        parse_these_chains_only=parse_these_chains_only,
        symmetry_residues=symmetry_residues,
        symmetry_weights=symmetry_weights,
        homo_oligomer=homo_oligomer,
        bias_AA_per_residue_jsonl=bias_AA_per_residue_jsonl,
        omit_AA_per_residue_jsonl=omit_AA_per_residue_jsonl,
        parse_atoms_with_zero_occupancy=parse_atoms_with_zero_occupancy,
    )
