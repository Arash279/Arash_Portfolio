export const projectGlances = {
  'verilog-code-similarity': {
    label: 'Verilog code → hardware-aware features → ML detector',
    problem: 'Copied hardware code is usually disguised, and text-matching tools such as MOSS miss most of it.',
    steps: [
      { icon: 'features', title: 'Hardware-aware features', detail: '8 features covering text, style, constants, branches and concurrent blocks.', tag: '+ 1 random sanity-check channel' },
      { icon: 'augment', title: 'Synthetic training data', detail: 'Gaussian Copula → conditional GAN to fill in the rare copied-code class.', tag: 'Beat SMOTE: 1.020 vs 0.769' },
      { icon: 'network', title: 'Classify & compare', detail: 'PyTorch classifier, tested against MOSS on a realistic 1:48 mix.', tag: 'PyTorch · ROC threshold' },
    ],
    result: '97%', metric: 'Copied pairs caught · F1 0.86 vs 0.32 for MOSS',
    outcome: 'A first-pass screen that helps protect chip-design IP: reviewers check a short list instead of the whole codebase.',
    note: 'B.Eng. Final Year Project, NUS (Suzhou) Research Institute. Selected for the Best Projects Showcase.',
    status: 'Completed · Best Projects Showcase',
  },
  'induction-motor': {
    label: 'One impedance sweep → circuit model → 20-second fit',
    problem: 'Textbook motor models stop working at the megahertz frequencies where drive EMI and insulation stress happen.',
    steps: [
      { icon: 'spectrum', title: 'One measurement sweep', detail: 'Terminal impedance of a 1.5 HP motor, 100 Hz to 100 MHz.', tag: '1,590 points · six decades' },
      { icon: 'circuit', title: 'Grow the circuit', detail: 'Extended a published circuit from 11 to 14 parameters with a resonant branch.', tag: 'Captures the high-frequency tail' },
      { icon: 'optimize', title: 'Fast, reliable fitting', detail: 'Log-space global search plus robust local polish, balanced across the band.', tag: '≈20 s on a laptop' },
    ],
    result: '≈20 s', metric: 'Full fit on a laptop · same answer every run',
    outcome: 'About 3× lower error than a standard single-algorithm fit, and the only method tested that is both accurate and repeatable.',
    note: 'NUS EE5003 M.Sc. project with Dr. Zhenyu Zhao. Measurements by the laboratory; model, fitting and analysis are my work.',
    status: 'Completed · August 2026',
  },
  'machine-modeling-review': {
    label: 'Published models → selection framework → design decisions',
    problem: 'Dozens of high-frequency motor models exist, with little guidance on which one answers which question.',
    steps: [
      { icon: 'taxonomy', title: 'Map the field', detail: 'Sort ≈93 papers by model type and by where parameters come from.', tag: 'Analytical · simulated · measured' },
      { icon: 'matrix', title: 'Compare the evidence', detail: 'Link each model to the outputs it can predict and how it was validated.', tag: 'Model × engineering purpose' },
      { icon: 'branch', title: 'Selection guidance', detail: 'Start from the output you need; choose model and test together.', tag: 'Terminal current ≠ internal voltage' },
    ],
    result: '≈93', metric: 'References in a co-authored journal review',
    outcome: 'A practical guide for choosing the simplest model, and the right test, for each engineering question.',
    note: 'Co-authored with Dr. Zhenyu Zhao (NUS). Manuscript under journal review; summary only until publication.',
    status: 'Under journal review',
  },
  'common-mode-choke': {
    label: 'A few measured chokes → align resonance → predict the rest',
    problem: 'Measuring every turn-count variant of an EMI choke is slow; naive blending smears the resonance.',
    steps: [
      { icon: 'audit', title: 'Clean test setup', detail: 'Develop on two cores, freeze the method, test once on a third.', tag: '10 references → 39 unseen chokes' },
      { icon: 'align', title: 'Align, then blend', detail: 'Shift curves so resonances line up, then interpolate magnitude and phase.', tag: 'No training · runs instantly' },
      { icon: 'diagnose', title: 'Measure smarter', detail: 'Spreading reference parts across the range cut error 2–6×.', tag: '18 combinations tested' },
    ],
    result: '12% lower', metric: 'Error than a published neural network · 39 unseen chokes',
    outcome: 'Mean error 0.083 vs 0.095, better on 27 of 39 parts, with a few lines of NumPy and no training.',
    note: 'Independent research on public NUS-EMBench data, compared with the published RANN predictions. Ongoing; November 2026 snapshot.',
    status: 'Ongoing · November 2026 snapshot',
  },
} as const;
