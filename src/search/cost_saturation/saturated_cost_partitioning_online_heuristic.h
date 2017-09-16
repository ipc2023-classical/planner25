#ifndef COST_SATURATION_SATURATED_COST_PARTITIONING_HEURISTIC_H
#define COST_SATURATION_SATURATED_COST_PARTITIONING_HEURISTIC_H

#include "cost_partitioning_generator.h"
#include "cost_partitioning_heuristic.h"

#include <memory>
#include <vector>

namespace cost_saturation {
class SaturatedCostPartitioningOnlineHeuristic : public CostPartitioningHeuristic {
    const std::shared_ptr<CostPartitioningGenerator> cp_generator;
    const int interval;
    const std::vector<int> costs;
    std::vector<std::vector<bool>> seen_facts;
    int num_evaluated_states;

    bool should_compute_scp(const State &state);
    virtual int compute_heuristic(const State &state) override;

public:
    explicit SaturatedCostPartitioningOnlineHeuristic(const options::Options &opts);
};
}

#endif
